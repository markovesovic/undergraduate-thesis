import numpy as np
import cv2 as cv
import time

import matplotlib.pyplot as plt
import matplotlib


# plt.xkcd()

def generate_for_box_plot(number_of_steps=10000, start_size=300, end_size=450, step=100, number_of_iterations=15):
    sequential_times = []
    parallel_times = []
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
            
        parallel_times.append(times)
        
        print('Sequential:\n')
        times = []
        for i in range(number_of_iterations):
            start = time.perf_counter()
            _ = simulator.sequential('gosper_gun')
            end = time.perf_counter()
            times.append(end - start)

        sequential_times.append(times)

        grid_sizes.append(grid_size)

    arr = []

    for arr1, arr2 in zip(sequential_times, parallel_times):

        local_arr = []
        for elem1 in arr1:
            for elem2 in arr2:
                local_arr.append(elem1 / elem2)

        arr.append(local_arr)
        
    print(arr)
    # plt.boxplot(arr)
    # plt.show()
    def save_to_file():
        with open('ratios.txt', 'w') as f:
            for a in arr:
                for v in a:
                    f.write(f'{v} ')
                f.write('\n')

    save_to_file()


def box_plot():
    data = []
    with open('ratios.txt', 'rb') as f:
        for line in f:
            values_string = (str(line)).split(' ')

            values = []

            for v in values_string:
                try:
                    values.append(float(v))
                except:
                    pass

            data.append(values)
    
    grid_sizes = []
    for i in range(300, 450, 100):
        grid_sizes.append(i)
        
    print('data: ', data)

    print('sizes: ', grid_sizes)
    
    # print(data)
    plt.boxplot(data, notch=True, meanline=True, labels=grid_sizes)
    plt.xlabel('Grid size')
    plt.ylabel('Times faster')
    plt.title('Ratios')
    plt.show()


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
    
    
def plot_with_fixed_steps(times=True, number_of_steps=10000, start_size=50, end_size=450, step=10):
    
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
    
    if times:
        showTimes()
    else:
        showRatio()
        
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



def plot_with_fixed_grid(times=True, grid_size=100, start_size=100, end_size=10000, step=100):

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
        
    if times:
        showTimes()
    else:
        showRatio()

    plt.show()
    

def generate_times_for_meshgrid():
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
                t = time.perf_counter() - start
                values_ret.append(round(t, 3))
            
            arr_ret.append(values_ret)
        
        return np.array(arr_ret)
    
    x = np.linspace(10, 10000, 20, dtype='int')
    y = np.linspace(50, 450, 20, dtype='int')

    X, Y = np.meshgrid(x, y)
    
    Z = calc(X, Y, 'sequential')
    
    Z1 = calc(X, Y, 'parallel')
    
    with open('X.npy', 'wb') as f:
        np.save(f, X)
    with open('Y.npy', 'wb') as f:
        np.save(f, Y)
    with open('Z.npy', 'wb') as f:
        np.save(f, Z)
    with open('Q.npy', 'wb') as f:
        np.save(f, Z1)
    
    
def load_mesh_grid_values():
    X = []
    Y = []
    Z = []
    Z1 = []
    with open('X.npy', 'rb') as f:
        X = np.load(f)
    with open('Y.npy', 'rb') as f:
        Y = np.load(f)
    with open('Z.npy', 'rb') as f:
        Z = np.load(f)
    with open('Q.npy', 'rb') as f:
        Z1 = np.load(f)
    
    return X, Y, Z, Z1
    
    
def plot_heatmap(which, min=None, max=None):
    
    def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
        
        if not ax:
            ax = plt.gca()

        im = ax.imshow(data, **kwargs)
        im.set_clim(min, max)

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


    def annotate_heatmap(im, data=None, valfmt="{x:.2f}", threshold=None, **textkw):

        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()

        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max())/2.

        kw = dict(horizontalalignment="center", verticalalignment="center")
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
    
    X, Y, Z, Z1 = load_mesh_grid_values()
                
    X1 = X[0]
    pom = []
    for row in Y:
        pom.append(row[0])
    Y1 = np.array(pom)
    fig, ax = plt.subplots()
    
    res = None
    
    if which == 1:
        res = Z1
    else:
        res = Z

    im, cbar = heatmap(res, X1, Y1, ax=ax, cmap="plasma", cbarlabel="speed in seconds")
    # texts = annotate_heatmap(im, valfmt="{x:.4f} s")
    texts = annotate_heatmap(im, valfmt="")

    fig.tight_layout()
    
    plt.show()
    
def plot_heatmap2():
    
    X, Y, Z, Z1 = load_mesh_grid_values()
    X1 = X[0]
    pom = []
    for row in Y:
        pom.append(row[0])
    Y1 = np.array(pom)
    
    fig, ax = plt.subplots()
    im = ax.imshow(Z)
    im.set_clim(0, 10)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(X1)), labels=X1)
    ax.set_yticks(np.arange(len(Y1)), labels=Y1)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(Y1)):
        for j in range(len(X1)):
            text = ax.text(j, i, "",
                        ha="center", va="center", color="w")

    ax.set_title("Harvest of local farmers (in tons/year)")
    fig.tight_layout()
    plt.show()
    

def plot_3d():
    X, Y, Z, Z1 = load_mesh_grid_values()
    
    ax = plt.axes(projection='3d')
    # ax.contour(X, Y, Z, 50, cmap='jet')
    # ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap='winter', edgecolor='none')
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot', edgecolor='none')
    ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap='turbo', edgecolor='none')
    ax.set_title('Time = simulate(number of steps, grid size)', fontsize=13)
    ax.set_xlabel('Number of steps', fontsize=10)
    ax.set_ylabel('Grid size in cells', fontsize=10)
    ax.set_zlabel('Time in seconds', fontsize=11)
        
    plt.show()


def main():
    # generate_times_with_fixed_steps()
    # plot_with_fixed_steps(False)
    # generate_times_with_fixed_grid()
    # plot_with_fixed_grid(True)
    
    # generate_times_for_meshgrid()
    # plot_3d()
    # plot_heatmap(2, 0, 30)
    # generate_for_box_plot()
    box_plot()

   

if __name__ == '__main__':
    main()
    