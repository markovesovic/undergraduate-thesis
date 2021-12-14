[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# OpenCV implementation of Game of Life

## Structure

- **/gof** - opencv source code module
- **/cv2** - generated python (3.7) module containing gof functionality
- **/gof/sample/main.py** - file for testing
- **/gof/sample/compare.py** - various comparation and visualization of algorithms
- **Generated plots** - few comparison examples visualized

## Usage

### a) Generating python module from source
- Download [openCV](https://github.com/opencv/opencv) source code 
- Add /gof to /modules directory 
- Generate build files with cmake
- Build and install with Visual Studio (make sure to include CMAKE_CXX_STANDARD=20)
- Full tutorial [here](https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html)

### b) Using already generated python lib
- Just add /cv2 dir to $PYTHON_PATH/Lib/site-packages/

### Running scripts
Run visualiation script:
```bash
python /gof/sample/main.py [number_of_steps] [grid_size] [shape]
```
- **number_of_steps** - number of iterations for algorithm to be simulated
- **grid_size** - size of torus space in cells, representing width and length
- **shape** - chose from number of predefined shapes:
    - 'r_pentomino'
    - 'glider'
    - 'gosper_gun'
    - 'growth'
    - 'oscilator'

Or just make yours!

### Comparation
1. Choose functionality you wonna use
2. Then run the following script
```bash
python /gof/sample/compare.py 
```
- Set of few functions for visualization of comparison between algorithms
- Couple of examples what you can make:
>![first_image](Generated%20plots/Figure_1.png)
>
>![second_image](Generated%20plots/Figure_10.png)
>
>![third_image](Generated%20plots/Figure_14.png)