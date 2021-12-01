#include "precomp.hpp"

namespace cv
{
    namespace gof
    {
        void simulator::init_steps(unsigned char* data)
        {
            for (auto step = 0; step < m_number_of_steps; step++)
            {
                unsigned char *matrix = data + step * (m_grid_size * m_grid_size);
                for (auto row = 0; row < m_grid_size; row++)
                {
                    for (auto column = 0; column < m_grid_size; column++)
                    {
                        *(matrix + row * m_grid_size + column) = 0;
                    }
                }
            }
        }

        void simulator::next_step(unsigned char* current, unsigned char* previous, int sum)
        {
            *current = *previous;
            if(*previous == 1)
            {
                if(sum < 2 || sum > 3)
                {
                    *current = 0;
                }
            }
            else if(sum == 3)
            {
                *current = 1;
            }
        }

        int simulator::calc_sum(unsigned char *previous_matrix, int row, int column)
        {
            int sum = 0;
            for (auto horizontal = -1; horizontal < 2; horizontal++)
            {
                for (auto vertical = -1; vertical < 2; vertical++)
                {
                    if (horizontal == 0 && horizontal == vertical)
                    {
                        continue;
                    }

                    sum += *(previous_matrix + 
                             normalize(row + horizontal) * m_grid_size +
                             normalize(column + vertical));
                }
            }
            return sum;
        }

        int simulator::normalize(int position)
        {
            if(position < 0)
                return m_grid_size - 1;
            if(position == m_grid_size)
                return 0;
            return position;
        }

        void simulator::print_progress(int step, int current_progress)
        {
            std::cout << "iter: " << step + 1 << " [";
            for(auto i = 0; i < current_progress; i++)
            {
                std::cout << "##";
            }
            for(auto i = current_progress; i < 10; i++)
            {
                std::cout << "**";
            }
            std::cout << "]" << std::endl;
        }

        void simulator::print_steps(unsigned char* data)
        {
            for(auto step = 0; step < m_number_of_steps; step++)
            {
                std::cout << "Step: " << step << std::endl;
                unsigned char* matrix = data + step * (m_grid_size * m_grid_size);

                for(auto row = 0; row < m_grid_size; row++)
                {
                    for(auto column = 0; column < m_grid_size; column++) 
                    {
                        std::cout << *(matrix + row * m_grid_size + column) << " ";
                    }
                    std::cout << std::endl;
                }
                std::cout << std::endl;
            }
        }

        void simulator::test_print(std::string message)
        {
            std::cout << message << std::endl;
        }

    } // gof
} // cv
