#include "precomp.hpp"

namespace cv
{
    namespace gof
    {
        simulator::simulator(int grid_size, int number_of_steps)
        {
            m_grid_size = grid_size;
            m_number_of_steps = number_of_steps;
        }

        void simulator::sequential(OutputArray out, std::string pattern)
        {
            auto start = std::chrono::high_resolution_clock::now();

            int _10th_of_progress = m_number_of_steps / 10.0;
            int current_step = _10th_of_progress;
            int current_progress = 1;

            // Create 3D matrix with given sizes
            cv::Mat steps(std::vector<int>{m_number_of_steps, m_grid_size, m_grid_size}, CV_8UC1);

            // Get pointer to matrix data
            unsigned char* input = steps.data;

            // Be sure to init steps - otherwise there will be some random mess
            this->init_steps(input);

            this->add_pattern(input, pattern);

            // Go through all steps
            for (auto step = 1; step < m_number_of_steps; step++)
            {
                // Get current and previous matrix for easier calculations
                unsigned char* matrix          = input +  step      * (m_grid_size * m_grid_size);
                unsigned char* previous_matrix = input + (step - 1) * (m_grid_size * m_grid_size);

                // Go through whole matrix in current step
                for (auto row = 0; row < m_grid_size; row++)
                {
                    for (auto column = 0; column < m_grid_size; column++)
                    {
                        // Calculate sum of all neighbour cells
                        auto sum = this->calc_sum(previous_matrix, row, column);

                        // Calculate value for next iteration
                        this->next_step(matrix + row * m_grid_size + column,
                                        previous_matrix + row * m_grid_size + column,
                                        sum);
                    }
                }
                // Print graphical representation of progress
                // Useful to track progress with large scale simulatons
                if (step >= current_step - 1)
                {
                    this->print_progress(step, current_progress++);
                    current_step += _10th_of_progress;
                }
            }

            // Log duration of algorithm
            auto stop = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

            std::cout << "Duration of algorithm: "
                      << duration.count()
                      << " ms"
                      << std::endl;

            // Return steps to python
            steps.copyTo(out);
        }

        // Struct for passing all neccesary parameters to thread worker
        struct workerConfig 
        {
            int id;
            std::vector<std::uint8_t> &payload;
            int number_of_steps;
            int grid_size;
            unsigned char *data;
            std::barrier<> *sync_point;
            simulator &sim;
        };

        void thread_worker(struct workerConfig workerConfig)
        {
            int id = workerConfig.id;
            auto payload = workerConfig.payload;
            int number_of_steps = workerConfig.number_of_steps;
            int grid_size = workerConfig.grid_size;
            unsigned char* data = workerConfig.data;
            auto sync_point = workerConfig.sync_point;
            auto sim = workerConfig.sim;

            int _10th_of_progress = number_of_steps / 10.0;
            int current_step = _10th_of_progress;
            int current_progress = 1;

            for(auto step = 1; step < number_of_steps; step++)
            {
                // Get current and previous matrix for easier calculations
                unsigned char *matrix =          data +  step      * (grid_size * grid_size);
                unsigned char *previous_matrix = data + (step - 1) * (grid_size * grid_size);

                for(auto & row : payload)
                {
                    for(auto column = 0; column < grid_size; column++)
                    {
                        auto sum = sim.calc_sum(previous_matrix, row, column);

                        // Calculate value for next iteration
                        sim.next_step(matrix + row * grid_size + column,
                                      previous_matrix + row * grid_size + column,
                                      sum);
                    }
                }

                sync_point->arrive_and_wait();

                // Print graphical representation of progress
                // Useful to track progress with large scale simulatons
                // Use only one thread for printing progress
                if(id == 0)
                {
                    if (step >= current_step - 1)
                    {
                        sim.print_progress(step, current_progress++);
                        current_step += _10th_of_progress;
                    }
                }
            }
        }

        void simulator::parallel(OutputArray out, std::string pattern)
        {
            auto start = std::chrono::high_resolution_clock::now();

            // Create 3D matrix with given sizes
            cv::Mat steps(std::vector<int>{m_number_of_steps, m_grid_size, m_grid_size}, CV_8UC1);

            // Get pointer to matrix data
            unsigned char *input = steps.data;

            // Be sure to init steps - otherwise there will be some random mess
            this->init_steps(input);

            // Add some pattern for better visualization
            this->add_pattern(input, pattern);

            // Processor count represents the maximum number of threads
            const auto processor_count = std::thread::hardware_concurrency();

            std::vector<std::thread> threads;

            std::vector<std::vector<std::uint8_t>> payloads(processor_count, std::vector<std::uint8_t>());

            // Distribute payload evenly to all accesible threads
            int i = 0;
            bool allPayloadsFull = false;
            for(auto row = 0; row < m_grid_size; row++)
            {
                payloads[i].push_back(row);
                i++;
                if(i == processor_count)
                {
                    i = 0;
                    allPayloadsFull = true;
                }
            }

            std::barrier sync_point(allPayloadsFull ? processor_count : i);

            // Start thread worker for each payload that was generated
            i = 0;
            for(auto & payload : payloads)            
            {
                if(!payload.empty())
                {
                    struct workerConfig conf = { i++, 
                                                 payload, 
                                                 m_number_of_steps, 
                                                 m_grid_size, 
                                                 input, 
                                                 &sync_point, 
                                                 *this };

                    threads.emplace_back(thread_worker, conf);
                }
            }

            // Wait for all working threads to finish
            for(auto & thread : threads)
            {
                thread.join();
            }

            // Log duration of algorithm
            auto stop = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);

            std::cout << "Duration of algorithm: "
                      << duration.count()
                      << " ms"
                      << std::endl;

            // Send matrix back to python
            steps.copyTo(out);
        }

    } // gof
} // cv