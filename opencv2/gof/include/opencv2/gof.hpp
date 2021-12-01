#ifndef __OPENCV_GOF_HPP__
#define __OPENCV_GOF_HPP__

#include <opencv2/imgproc.hpp>
#include <iostream>
#include <vector>
#include <barrier>

namespace cv {
namespace gof {

class CV_EXPORTS_W simulator
{
private:
    // Represents size of grid that the simulation will be run for
    int m_grid_size;
    // Represents the number of frames that will be in simulation
    int m_number_of_steps;

public:
    CV_WRAP simulator(int grid_size, int number_of_steps);
    virtual ~simulator() {}

    // Functions for simulation
    CV_WRAP void parallel(OutputArray out, std::string pattern);
    CV_WRAP void sequential(OutputArray out, std::string pattern);

    /*
        Helper funcs
    */

    // Enables folding grid in torus
    int normalize(int position);
    // Populates first matrix in row with 0s
    void init_steps(unsigned char* data);
    // Calculates value for current cell
    void next_step(unsigned char* previous, unsigned char* current, int sum);
    // Calculate neighbour sum for given cell with position of (row, column)
    int calc_sum(unsigned char* previous_matrix, int row, int column);
    // Pretty-print of all steps
    void print_steps(unsigned char* data);
    // Visual representation of simulation progress
    void print_progress(int step, int current_progress);

    /*
        Funcs for adding predefined interesting shapes for simulation
    */

    void add_pattern(unsigned char* data, std::string pattern);
    void add_glider(unsigned char* data);
    void add_oscilator(unsigned char* data);
    void add_gosper_glider_gun(unsigned char* data);
    void add_r_pentomino(unsigned char* data);
    void add_infinite_growth(unsigned char* data);

    void test_print(std::string message);
};

} // gof
} // cv

#endif
