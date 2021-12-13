[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Bachelor's Degree Thesis - Game of Life

Comparing performance of two different C++ implementations of [John Conway](http://en.wikipedia.org/wiki/John_Horton_Conway)'s [**Game of Life**](http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). 
- Trivial sequential implementation done by looping through whole grid and calculating each cell's value one at a time
- Parallel implementation done by splitting grid into smaller subgrids, and calculating multiple cell's value at the same time


## OpenCV

- Module written in [OpenCV](https://github.com/opencv/opencv) library
- Passing generated arrays from C++ to python via library's python bindings
- Extremely fast conversion from C++ to python numpy arrays


## Pybind11

- Source files written in C++ 
- Transformed in python module via [pybind11](https://pypi.org/project/pybind11/) bindings
- Slower conversion from C++ to python numpy arrays
