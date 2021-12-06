import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt

# Optional
plt.xkcd()


def fixed_steps():
    
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


def fixed_grid():
    
    grid_size = 100
    number_of_iterations = 1
    start_size = 100
    end_size = 10000
    step = 1000
    
    parallel_times = []
    sequential_times = []
    numbers_of_steps = []
    
    for step in range(start_size, end_size, step):
        
        print(f'\n\nNumber of step: {step}:\n\n')
        simulator = cv.gof_simulator(grid_size, step)

        
        print('Parallel:\n')
        times = []
        for _ in range(number_of_iterations):
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
        for _ in range(number_of_iterations):
            start = time.perf_counter()
            _ = simulator.sequential('gosper_gun')
            end = time.perf_counter()
            times.append(end - start)

        sum = 0
        for item in times:
            sum += item
        sum /= number_of_iterations
        sequential_times.append(sum)


        numbers_of_steps.append(step)


    print('Parallel times')
    for (size, t) in zip(numbers_of_steps, parallel_times): 
        print(f'{size}: { round(t, 3) }, ', end='')
        
    print('\nSequential times')
    for (size, t) in zip(numbers_of_steps, sequential_times):
        print(f'{size}: { round(t, 3) } ', end='')


    def showTimes():
        plt.title(f'Parallel and sequential execution speed for {grid_size}x{grid_size} grid')
        plt.plot(numbers_of_steps, sequential_times, '-g', label='Sequential algorithm')
        plt.xlabel('Number of steps')
        plt.plot(numbers_of_steps, parallel_times, '-b', label='Parallel algorithm')
        plt.ylabel('Time(s)')
        plt.legend()


    def showRatio():
        ratios = []
        for p_t, s_t in zip(parallel_times, sequential_times):
            ratios.append(s_t / p_t)

        plt.title(f'Ratio between parallel and sequential speeds for {grid_size}x{grid_size} grid')
        plt.plot(numbers_of_steps, ratios, '-r', label='Ratio')    
        plt.xlabel('Grid size(cells)')
        plt.ylabel('Times faster')
        
    # showRatio()
    showTimes()

    plt.show()

import random

def test():
    
    parallel_times = []
    sequential_times = []

    steps = []
    sizes = []
    
    # for step in range(100, 1000, 100):
    #     steps.append(step)
        
    # for size in range(10, 100, 10):
    #     sizes.append(size)
    
    for _ in range(50):
        sizes.append(random.randrange(10, 450, 10))
        steps.append(random.randrange(100, 10000, 250))
    
        
    for step, size in zip(steps, sizes):
        simulator = cv.gof_simulator(size, step)

        start = time.perf_counter()
        _ = simulator.parallel('gosper_gun')
        parallel_times.append(time.perf_counter() - start)
        
        start = time.perf_counter()
        _ = simulator.sequential('gosper_gun')
        sequential_times.append(time.perf_counter() - start)


    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(steps, sizes, parallel_times,
            linewidths=1, alpha=.7,
            edgecolor='k',
            s=200,
            marker='p',
            label='parallel',
            c=parallel_times)

    ax.scatter(steps, sizes, sequential_times,
               linewidths=2, alpha=.9,
               edgecolor='r',
               s=200,
               marker='s',
               label='sequential',
               c=sequential_times)
    plt.show()


def main():
    test()
    

if __name__ == '__main__':
    main()
    