import numpy as np
import cv2 as cv
import time
import sys

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


def animate(steps):
  def init():
    im.set_data(steps[0])
    return [im]

  def animate(i):
    im.set_data(steps[i])
    return [im]

  im = plt.matshow(steps[0], interpolation='None', animated=True)

  anim = FuncAnimation(im.get_figure(), animate, init_func=init,
                       frames=len(steps), interval=10, blit=True, repeat=False)
  return anim


def main():
    SHAPES = ['r_pentomino', 'glider', 'gosper_gun', 'oscilator', 'growth']
    np.set_printoptions(sys.maxsize)

    # Number of iteration to simulate
    number_of_steps = 1000
    # Size of grid space in squares
    grid_size = 150
    # Pattern for simulation
    shape = SHAPES[2]

    num_of_args = len(sys.argv)
    
    if num_of_args > 1:
      number_of_steps = int(sys.argv[1])
    if num_of_args > 2:
      grid_size = int(sys.argv[2])
    if num_of_args > 3:
      shape = sys.argv[3]      
    

    simulator = cv.gof_simulator(grid_size, number_of_steps)
    
    start = time.perf_counter()
    
    steps = simulator.sequential(shape)
    # steps = simulator.parallel(shape)
    
    # print(steps)
  
    print(f'Time: {round(time.perf_counter() - start, 3)} s')

    # * Visualization using matplotlib
    anim = animate(steps)
    # figManager = plt.get_current_fig_manager()
    # figManager.full_screen_toggle()
    plt.show()
    
if __name__ == '__main__':
    main()
    
