import sys
import time
import numpy as np
import game_of_life_simulator as gof


from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

# np.set_printoptions(threshold=sys.maxsize)

def animate(steps):
  def init():
    im.set_data(steps[0])
    return [im]

  def animate(i):
    im.set_data(steps[i])
    return [im]

  im = plt.matshow(steps[0], interpolation='None', animated=True)

  anim = FuncAnimation(im.get_figure(), animate, init_func=init,
                       frames=len(steps), interval=2, blit=True, repeat=False)
  return anim



def main():
    # Number of iteration to simulate
    number_of_steps = 50000
    # Size of grid space in squares
    grid_size = 100
    
    # Possible patterns for simulation
    possible_patterns = [
      'random',
      'gosper_glider_gun',
      'unbounded_growth',
      'infinite_growth',
      'r_pentomino',
      'bloom',
      'accorn',
      '23334m',
      'lidka',
      'queen_bee',
    ]
    
    start = time.perf_counter()
    
    # * Run cpp algorithm and retrieve result in steps var
    steps_parallel = gof.calculate_steps_parallel(number_of_steps, grid_size, possible_patterns[5])
  
    print(f'Parallel algorithm took: {round(time.perf_counter() - start, 3)} s')

    # print(steps_parallel)
    
    # * Visualization using matplotlib
    anim = animate(steps_parallel)
    # figManager = plt.get_current_fig_manager()
    # figManager.full_screen_toggle()
    plt.show()
    
    # start = time.perf_counter()
    # gof.calculate_steps_sequential(number_of_steps, grid_size, possible_patterns[3])

    # print(f'Sequential algorithm took: {round(time.perf_counter() - start, 3)} ms')

    # print((steps_parallel==steps_sequential).all())

if __name__ == '__main__':
    main()
    
