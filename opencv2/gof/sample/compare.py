import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt

# Optional
plt.xkcd()


def main():
    
    number_of_steps = 10000
    number_of_iterations = 5
    start_size = 50
    end_size = 450
    step = 10
    
    parallel_times = []
    sequential_times = []
    grid_sizes = []
    
    for grid_size in range(start_size, end_size, step):
        
        print(f'\n\nGrid size: {grid_size}:\n\n')
        simulator = cv.gof_simulator(grid_size, number_of_steps)

        
        print('Parallel:\n')
        times = []
        for i in range(number_of_iterations):
            start = time.perf_counter()
            _ = simulator.parallel('gosper_gun')
            end = time.perf_counter()
            times.append(end - start)
            
        sum = 0
        for item in times:
            sum += item
        sum /= number_of_iterations
        parallel_times.append(sum)
        
        
        print('Sequential:\n')
        for i in range(number_of_iterations):
            start = time.perf_counter()
            _ = simulator.sequential('gosper_gun')
            end = time.perf_counter()
            times.append(end - start)

        sum = 0
        for item in times:
            sum += item
        sum /= number_of_iterations
        sequential_times.append(sum)


        grid_sizes.append(grid_size)


    print('Parallel times')
    for (size, t) in zip(grid_sizes, parallel_times): 
        print(f'{size}: { round(t, 3) }, ', end='')
        
    print('\nSequential times')
    for (size, t) in zip(grid_sizes, sequential_times):
        print(f'{size}: { round(t, 3) } ', end='')


    def showTimes():
        plt.title(f'Parallel and sequential execution speed for {number_of_steps} steps')
        plt.plot(grid_sizes, sequential_times, '-g', label='Sequential algorithm')
        plt.xlabel('Grid size(cells)')
        plt.plot(grid_sizes, parallel_times, '-b', label='Parallel algorithm')
        plt.ylabel('Time(s)')
        plt.legend()


    def showRatio():
        ratios = []
        for p_t, s_t in zip(parallel_times, sequential_times):
            ratios.append(s_t / p_t)

        plt.title(f'Ratio between parallel and sequential speeds for {number_of_steps} steps')
        plt.plot(grid_sizes, ratios, '-r', label='Ratio')    
        plt.xlabel('Grid size(cells)')
        plt.ylabel('Times faster')
    
    # showRatio()
    showTimes()
    
    plt.show()


if __name__ == '__main__':
    main()
    