#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include <iostream>
#include <vector>
#include <random>
#include <thread>
#include <barrier>
#include <sstream>


using namespace std;


vector<vector<vector<uint8_t>>> initialize_steps(const int number_of_steps, 
                                                 const int grid_size,
                                                 const bool random = true)
{

    random_device dev;
    mt19937 mt(dev());
    uniform_int_distribution<mt19937::result_type> dist(0, 1);

    vector<vector<vector<uint8_t>>>
        out(number_of_steps, vector<vector<uint8_t>>(grid_size, vector<uint8_t>(grid_size)));

    for (auto &step : out)
    {
        for (auto &row : step)
        {
            for (auto &c : row)
            {
                c = random ? dist(mt) : 0;
            }
        }
    }
    return out;
}

void add_oscillator(vector<vector<vector<uint8_t>>>& steps)
{
    steps[0][2][1] = 1;
    steps[0][2][2] = 1;
    steps[0][2][3] = 1;
}


void add_glider(vector<vector<vector<uint8_t>>>& steps)
{
    steps[0][2][3] = 1;
    steps[0][3][1] = 1;
    steps[0][3][3] = 1;
    steps[0][4][2] = 1;
    steps[0][4][3] = 1;
}

void add_r_pentomino(vector<vector<vector<uint8_t>>>& steps, const int x, const int y) 
{
    steps[0][x + 1][y + 2] = 1;
    steps[0][x + 1][y + 3] = 1;
    steps[0][x + 2][y + 1] = 1;
    steps[0][x + 2][y + 2] = 1;
    steps[0][x + 3][y + 2] = 1;
}

void add_bloom(vector<vector<vector<uint8_t>>>& steps, const int x, const int y)
{
    steps[0][x + 1][y + 1] = 1;
    steps[0][x + 1][y + 12] = 1;
    steps[0][x + 2][y + 2] = 1;
    steps[0][x + 2][y + 3] = 1;
    steps[0][x + 2][y + 4] = 1;
    steps[0][x + 2][y + 5] = 1;
    steps[0][x + 2][y + 12] = 1;
    steps[0][x + 3][y + 3] = 1;
    steps[0][x + 3][y + 4] = 1;
    steps[0][x + 3][y + 12] = 1;
    steps[0][x + 4][y + 11] = 1;
    steps[0][x + 5][y + 9] = 1;
    steps[0][x + 5][y + 11] = 1;
}

void add_acorn(vector<vector<vector<uint8_t>>>& steps, const int x, const int y)
{
    steps[0][x + 1][y + 2] = 1;
    steps[0][x + 2][y + 4] = 1;
    steps[0][x + 3][y + 1] = 1;
    steps[0][x + 3][y + 2] = 1;
    steps[0][x + 3][y + 5] = 1;
    steps[0][x + 3][y + 6] = 1;
    steps[0][x + 3][y + 7] = 1;
}


void add_23334m(vector<vector<vector<uint8_t>>>& steps, const int x, const int y) 
{
    steps[0][x + 1][y + 3] = 1;
    steps[0][x + 2][y + 1] = 1;
    steps[0][x + 2][y + 2] = 1;
    steps[0][x + 3][y + 2] = 1;
    steps[0][x + 4][y + 1] = 1;
    steps[0][x + 4][y + 4] = 1;
    steps[0][x + 5][y + 5] = 1;
    steps[0][x + 6][y + 2] = 1;
    steps[0][x + 6][y + 5] = 1;
    steps[0][x + 7][y + 3] = 1;
    steps[0][x + 7][y + 5] = 1;
    steps[0][x + 8][y + 2] = 1;
}

void add_queen_bee(vector<vector<vector<uint8_t>>>& steps, const int x, const int y) 
{
    steps[0][x + 1][y + 1] = 1;
    steps[0][x + 2][y + 1] = 1;
    steps[0][x + 2][y + 3] = 1;
    steps[0][x + 3][y + 2] = 1;
    steps[0][x + 3][y + 4] = 1;
    steps[0][x + 4][y + 2] = 1;
    steps[0][x + 4][y + 5] = 1;
    steps[0][x + 5][y + 2] = 1;
    steps[0][x + 5][y + 4] = 1;
    steps[0][x + 6][y + 1] = 1;
    steps[0][x + 6][y + 3] = 1;
    steps[0][x + 7][y + 1] = 1;
}

void add_lidka(vector<vector<vector<uint8_t>>> &steps, const int x, const int y)
{
    steps[0][x + 1][y + 2] = 1;
    steps[0][x + 2][y + 1] = 1;
    steps[0][x + 2][y + 3] = 1;
    steps[0][x + 3][y + 2] = 1;
    steps[0][x + 11][y + 9] = 1;
    steps[0][x + 12][y + 7] = 1;
    steps[0][x + 12][y + 9] = 1;
    steps[0][x + 13][y + 6] = 1;
    steps[0][x + 13][y + 7] = 1;
    steps[0][x + 13][y + 9] = 1;
    steps[0][x + 15][y + 5] = 1;
    steps[0][x + 15][y + 6] = 1;
    steps[0][x + 15][y + 7] = 1;
}

void add_infinite_growth(vector<vector<vector<uint8_t>>>&steps, const int x, const int y)
{
    steps[0][x + 1][y + 7] = 1;
    steps[0][x + 2][y + 5] = 1;
    steps[0][x + 2][y + 7] = 1;
    steps[0][x + 2][y + 8] = 1;
    steps[0][x + 3][y + 5] = 1;
    steps[0][x + 3][y + 7] = 1;
    steps[0][x + 4][y + 5] = 1;
    steps[0][x + 5][y + 3] = 1;
    steps[0][x + 6][y + 1] = 1;
    steps[0][x + 6][y + 3] = 1;
}


void add_gosper_glider_gun(vector<vector<vector<uint8_t>>>& steps) 
{
    steps[0][5][1] = steps[0][5][2] = 1;
    steps[0][6][1] = steps[0][6][2] = 1;

    steps[0][3][13] = steps[0][3][14] = 1;
    steps[0][4][12] = steps[0][4][16] = 1;
    steps[0][5][11] = steps[0][5][17] = 1;
    steps[0][6][11] = steps[0][6][15] = steps[0][6][17] = steps[0][6][18] = 1;
    steps[0][7][11] = steps[0][7][17] = 1;
    steps[0][8][12] = steps[0][8][16] = 1;
    steps[0][9][13] = steps[0][9][14] = 1;

    steps[0][1][25] = 1;
    steps[0][2][23] = steps[0][2][25] = 1;
    steps[0][3][21] = steps[0][3][22] = 1;
    steps[0][4][21] = steps[0][4][22] = 1;
    steps[0][5][21] = steps[0][5][22] = 1;
    steps[0][6][23] = steps[0][6][25] = 1;
    steps[0][7][25] = 1;

    steps[0][3][35] = steps[0][3][36] = 1;
    steps[0][4][35] = steps[0][4][36] = 1;
}


void add_unbounded_growth(vector<vector<vector<uint8_t>>>& steps, const int x, const int y) 
{
    steps[0][x + 2][y + 1] = 1;
    steps[0][x + 2][y + 2] = 1;
    steps[0][x + 2][y + 3] = 1;
    steps[0][x + 2][y + 5] = 1;
    steps[0][x + 3][y + 1] = 1;
    steps[0][x + 4][y + 4] = 1;
    steps[0][x + 4][y + 5] = 1;
    steps[0][x + 5][y + 2] = 1;
    steps[0][x + 5][y + 3] = 1;
    steps[0][x + 5][y + 5] = 1;
    steps[0][x + 6][y + 1] = 1;
    steps[0][x + 6][y + 3] = 1;
    steps[0][x + 6][y + 5] = 1;
}

// Adding predefined figures to initial grid
vector<vector<vector<uint8_t>>> initialize_steps_with_predefined_figures(const int number_of_steps, 
                                                                         const int grid_size, 
                                                                         const string& pattern) 
{
    if (pattern == "random" || pattern.empty())
    {
        return initialize_steps(number_of_steps, grid_size, true);
    }

    auto steps = initialize_steps(number_of_steps, grid_size, false);

    if (pattern == "oscillator")
    {
        add_oscillator(steps);
    }
    else if (pattern == "glider")
    {
        add_glider(steps);
    }
    else if (pattern == "gosper_glider_gun")
    {
        add_gosper_glider_gun(steps);
    }
    else if (pattern == "unbounded_growth")
    {
        add_unbounded_growth(steps, grid_size / 2, grid_size / 2);
    } 
    else if(pattern == "r_pentomino")
    {
        add_r_pentomino(steps, grid_size / 2, grid_size / 2);
    }
    else if(pattern == "bloom")
    {
        add_bloom(steps, grid_size / 2, grid_size / 2);
    }
    else if(pattern == "acorn") 
    {
        add_acorn(steps, grid_size / 2, grid_size / 2);
    }
    else if(pattern == "23334m")
    {
        add_23334m(steps, grid_size / 2, grid_size / 2);
    } 
    else if(pattern == "lidka")
    {
        add_lidka(steps, grid_size / 2, grid_size / 2);
    }
    else if(pattern == "queen_bee")
    {
        add_queen_bee(steps, grid_size / 2, grid_size / 2);
    }
    else if(pattern == "infinite_growth")
    {
        add_infinite_growth(steps, grid_size / 2, grid_size / 2);
    }
    else 
    {
        cout << "Invalid pattern!" << endl;
        exit(-1);
    }
    return steps;
}

// Util function to print all steps
void print_steps(const vector<vector<vector<uint8_t>>>& steps)
{
    for (auto &step : steps)
    {
        for (auto &row : step)
        {
            for (auto &c : row)
            {
                cout << unsigned(c) << " ";
            }
            cout << endl;
        }
        cout << endl
             << endl;
    }
}

// Util function to enable bending grid in torus (donut)
int normalize(const int position, const int grid_size)
{
    if (position < 0)
    {
        return grid_size - 1;
    }
    if (position == grid_size)
    {
        return 0;
    }
    return position;
}

// Util function to print progress
void print_progress(const int step, const int current_progress)
{
    {
        cout << "iter: " << step + 1 << " [";
        for (auto i = 0; i < current_progress; i++)
        {
            cout << "##";
        }
        for (auto i = current_progress; i < 10; i++)
        {
            cout << "**";
        }
        cout << "]" << endl;
    }
}

// Trivial sequential implementation of game of life 
vector<vector<vector<uint8_t>>> calculate_steps_sequential(const int number_of_steps,
                                                           const int grid_size,
                                                           const string &pattern = "")
{

    auto start = chrono::high_resolution_clock::now();

    auto steps = initialize_steps_with_predefined_figures(number_of_steps, grid_size, pattern);

    int _10th_of_progress = number_of_steps / 10.0;
    int current_step = _10th_of_progress;
    int current_progress = 1;

    for (auto step = 1; step < number_of_steps; step++)
    {
        for (auto row = 0; row < grid_size; row++)
        {
            for (auto column = 0; column < grid_size; column++)
            {
                auto sum = 0;

                for (auto horizontal = -1; horizontal < 2; horizontal++)
                {
                    for (auto vertical = -1; vertical < 2; vertical++)
                    {
                        // Skip central field
                        if (horizontal == vertical && vertical == 0)
                        {
                            continue;
                        }
                        // Calculate sum
                        sum += steps[step - 1]
                                    [normalize(row + horizontal, grid_size)]
                                    [normalize(column + vertical, grid_size)];
                    }
                }

                steps[step][row][column] = steps[step - 1][row][column];

                if (steps[step - 1][row][column] == 1)
                {
                    if (sum < 2 || sum > 3)
                    {
                        steps[step][row][column] = 0;
                    }
                }
                else if (sum == 3)
                {
                    steps[step][row][column] = 1;
                }
            }
        }

        if (step >= current_step - 1)
        {
            print_progress(step, current_progress);
            current_progress++;
            current_step += _10th_of_progress;
        }
    }

    auto stop = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);

    cout << "Duration of algorithm: "
         << (duration.count())
         << " ms"
         << endl;

    return steps;
}

void thread_worker(const int id,
                   vector<uint8_t> &payload,
                   const int number_of_steps,
                   const int grid_size,
                   vector<vector<vector<uint8_t>>> &steps,
                   barrier<> &sync_point)
{
    // Stuff for visual representation of progress
    int _10th_of_progress = number_of_steps / 10.0;
    int current_step = _10th_of_progress;
    int current_progress = 1;

    // Iterate through each step
    for (auto step = 1; step < number_of_steps; step++)
    {
        // Go through all rows that are in payload
        for (auto &row : payload)
        {
            // Go through every column in that row
            for (auto column = 0; column < grid_size; column++)
            {
                // Number of living cell around current cell
                auto sum = 0;

                // Go check every neighbour cell
                for (auto horizontal = -1; horizontal < 2; horizontal++)
                {
                    for (auto vertical = -1; vertical < 2; vertical++)
                    {
                        // Skip central field
                        if (horizontal == vertical && vertical == 0)
                            continue;

                        // Add neighbour cell state to sum
                        sum += steps[step - 1]
                                    [normalize(row + horizontal, grid_size)]
                                    [normalize(column + vertical, grid_size)];
                    }
                }

                steps[step][row][column] = steps[step - 1][row][column];

                // Just game of life logic to determine cell state in next iteration
                if (steps[step - 1][row][column] == 1)
                {
                    if (sum < 2 || sum > 3)
                    {
                        steps[step][row][column] = 0;
                    }
                }
                else if (sum == 3)
                {
                    steps[step][row][column] = 1;
                }
            }
        }

        // Synchronization between iterations
        // All threads must finish current iteration before next one can start
        sync_point.arrive_and_wait();

        // One thread just prints progress to screen
        if(id == 0) 
        {
            if (step >= current_step - 1)
            {
                print_progress(step, current_progress);
                current_progress++;
                current_step += _10th_of_progress;
            }
        }
    }
}

vector<vector<vector<uint8_t>>> calculate_steps_parallel(const int number_of_steps,
                                                         const int grid_size,
                                                         const string &pattern = "")
{

    auto start = chrono::high_resolution_clock::now();

    // Initialize steps with given pattern
    // Default will be random grid
    auto steps = initialize_steps_with_predefined_figures(number_of_steps, grid_size, pattern);

    // Get number of available threads
    const auto processor_count = thread::hardware_concurrency();

    vector<thread> threads;

    // Each payload contains numbers of rows from grid that will be given to each thread
    vector<vector<uint8_t>> payloads(processor_count, vector<uint8_t>());


    // 
    int i = 0;
    bool allPayloadsFull = false;
    for (auto row = 0; row < grid_size; row++)
    {
        payloads[i].push_back(row);
        i++;
        if (i == processor_count)
        {
            i = 0;
            allPayloadsFull = true;
        }
    }

    barrier sync_point(allPayloadsFull ? processor_count : i);

    // Starting threads
    i = 0;
    for (auto &payload : payloads)
    {
        if (payload.empty())
        {
            continue;
        }
        threads.emplace_back(thread_worker,
                             i++,
                             ref(payload),
                             number_of_steps,
                             grid_size,
                             ref(steps),
                             ref(sync_point));
    }

    // Waiting all threads to finish
    for (auto &t : threads)
    {
        t.join();
    }

    auto stop = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::milliseconds>(stop - start);


    cout << "Duration of algorithm: "
         << (duration.count())
         << " ms"
         << endl;

    cout << "All worker threads finished!" << endl;
    return steps;
}

// Define python module that will be created
PYBIND11_MODULE(game_of_life_simulator, mod)
{

    mod.def("calculate_steps_parallel",
     [](const int number_of_steps, const int grid_size, const string& pattern = "") { 
        pybind11::array out = 
            pybind11::cast(calculate_steps_parallel(number_of_steps, grid_size, pattern));
        return out;
    }, "This calculates steps parallel");

    mod.def("calculate_steps_sequential",
     [](const int number_of_steps, const int grid_size, const string& pattern = "") {
        pybind11::array out = 
            pybind11::cast(calculate_steps_sequential(number_of_steps, grid_size, pattern));
        return out;
    }, "This calculates steps sequential");
}

