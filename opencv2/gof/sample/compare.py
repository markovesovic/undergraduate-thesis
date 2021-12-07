import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt
import matplotlib


plt.xkcd()


def generate_times_with_fixed_steps(number_of_steps=10000, start_size=50, end_size=450, step=10, number_of_iterations=3):
    
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

    def save_to_file():
        with open('parallel_times_fixed_step.txt', 'w') as f:
            for v in parallel_times:
                f.write(f'{v}\n')
                
        with open('sequential_times_fixed_step.txt', 'w') as f:
            for v in sequential_times:
                f.write(f'{v}\n')

    save_to_file()
    
    
def plot_with_fixed_steps(number_of_steps=10000, start_size=50, end_size=450, step=10):
    
    grid_sizes = []
    sequential_times = []
    parallel_times = []
    
    for i in range(start_size, end_size, step):
        grid_sizes.append(i)
    
    with open('parallel_times_fixed_step.txt', 'r') as f:
        for line in f:
            parallel_times.append(float(line))
    with open('sequential_times_fixed_step.txt', 'r') as f:
        for line in f:
            sequential_times.append(float(line))
    
    
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
    
    showTimes()
    plt.show()
    

def generate_times_with_fixed_grid(grid_size=100, start_size=100, end_size=10000, step=100, number_of_iterations=3):
    
    parallel_times = []
    sequential_times = []
    
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


    def save_to_file():
        with open('parallel_times_fixed_grid.txt', 'w') as f:
            for v in parallel_times:
                f.write(f'{v}\n')
                
        with open('sequential_times_fixed_grid.txt', 'w') as f:
            for v in sequential_times:
                f.write(f'{v}\n')

    save_to_file()



def plot_with_fixed_grid(grid_size=100, start_size=100, end_size=10000, step=100):

    numbers_of_steps = []
    sequential_times = []
    parallel_times = []
    
    for i in range(start_size, end_size, step):
        numbers_of_steps.append(i)
    
    with open('parallel_times_fixed_grid.txt', 'r') as f:
        for line in f:
            parallel_times.append(float(line))
    with open('sequential_times_fixed_grid.txt', 'r') as f:
        for line in f:
            sequential_times.append(float(line))

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
    


def test():

    def calc(x, y, algorithm):
        arr_ret = []
        for arr_x, arr_y in zip(x, y):
            values_ret = []
            for value_x, value_y in zip(arr_x, arr_y):
                
                start = time.perf_counter()
                if algorithm == 'parallel':
                    cv.gof_simulator(value_y, value_x).parallel('gosper_gun')
                else:
                    cv.gof_simulator(value_y, value_x).sequential('gosper_gun')
                # cv.gof_simulator(value_y, value_x).sequential('gosper_gun')
                t = time.perf_counter() - start
                values_ret.append(round(t, 3))
            
            arr_ret.append(values_ret)
        
        return np.array(arr_ret)
    
    
    def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
        
        if not ax:
            ax = plt.gca()

        im = ax.imshow(data, **kwargs)

        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
        ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

        ax.tick_params(top=True, bottom=False,
                    labeltop=True, labelbottom=False)

        plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
                rotation_mode="anchor")

        ax.spines[:].set_visible(False)
        
        ax.set_title('Speed of execution for grid size and number of iterations')

        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)
        
        return im, cbar


    def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                        threshold=None, **textkw):

        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()

        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max())/2.

        kw = dict(horizontalalignment="center",
                verticalalignment="center")
        kw.update(textkw)

        if isinstance(valfmt, str):
            valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color='black')
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
                texts.append(text)

        return texts
                
                
    x = np.linspace(10, 1000, 10, dtype='int')
    y = np.linspace(50, 150, 10, dtype='int')

    X, Y = np.meshgrid(x, y)
    
    Z = calc(X, Y, 'sequential')
    
    Z1 = calc(X, Y, 'parallel')

    def plot_3d():
        ax = plt.axes(projection='3d')
        # ax.contour(X, Y, Z, 50, cmap='jet')
        ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap='inferno', edgecolor='none')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='plasma', edgecolor='none')
        ax.set_title('Time = simulate(number of steps, grid size)', fontsize=13)
        ax.set_xlabel('Number of steps', fontsize=10)
        ax.set_ylabel('Grid size in cells', fontsize=10)
        ax.set_zlabel('Time in seconds', fontsize=11)
        
        
    def plot_heatmap():
        X1 = X[0]
        pom = []
        for row in Y:
            pom.append(row[0])
        Y1 = np.array(pom)
        fig, ax = plt.subplots()

        im, cbar = heatmap(Z1, X1, Y1, ax=ax, cmap="plasma", cbarlabel="speed in seconds")
        texts = annotate_heatmap(im, valfmt="{x:.4f} s")

        fig.tight_layout()


    # plot_3d()
    plot_heatmap()
    
    plt.show()


def main():
    # test()
    # generate_times_with_fixed_steps()
    # plot_with_fixed_steps()
    # generate_times_with_fixed_grid()
    plot_with_fixed_grid()

    

if __name__ == '__main__':
    main()
    