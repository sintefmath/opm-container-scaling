from .get_runtime import get_runtimes
import json
import matplotlib.pyplot as plt
import numpy as np


def plot_scalings(configuration_files, skip_missing=True, save_to_file=None, show=True, time_key='Total time', per_quantity=None):
    
    
    symbols = ['-o', '-*', '-x']
    for n, configuration_file in enumerate(configuration_files):
        with open(configuration_file) as f:
            configuration = json.load(f)
        runtimes = get_runtimes(configuration, skip_missing=skip_missing, time_key=time_key, per_quantity=per_quantity)

        number_of_processes_list = np.array(list(map(int, configuration['number_of_processes_list'])), dtype=np.float64)

        runtimes_procs = zip(runtimes, number_of_processes_list)
        

        filtered_runtimes_procs = list(filter(lambda p: p[0] >= 0, runtimes_procs))
        runtimes = np.array([p[0] for p in filtered_runtimes_procs])
        number_of_processes_list = np.array([p[1] for p in filtered_runtimes_procs])

        plt.figure(1)
        plt.loglog(number_of_processes_list,
                   runtimes, symbols[n%len(symbols)], label=configuration_file)

        plt.figure(2)
        ideal_runtimes = runtimes[0] * number_of_processes_list[0] / number_of_processes_list
        efficiency = ideal_runtimes / runtimes
        plt.loglog(number_of_processes_list,
                   efficiency, symbols[n%len(symbols)], label=configuration_file)

    plt.figure(1)    
    plt.loglog(number_of_processes_list, 
               runtimes[0] * number_of_processes_list[0] * number_of_processes_list**(-1),
               '--', label='Ideal')
    
    if per_quantity is None:
        plt.ylabel(f'{time_key} [s]')
    else:
        plt.ylabel(f'{time_key} per {per_quantity} [s/it]')
    
    plt.xlabel('Number of processes')
    plt.grid(True)
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.legend()
     
    if save_to_file is not None:
        plt.savefig(save_to_file + "_runtime.png")

    plt.figure(2)
    plt.loglog(number_of_processes_list, 
               np.ones_like(number_of_processes_list),
               '--', label='Ideal')
    
    plt.ylabel('Efficiency')
    plt.xlabel('Number of processes')
    plt.grid(True)
    plt.xscale('log', base=2)
    plt.yscale('linear')
    plt.legend()
    if show:
        plt.show()
        
    if save_to_file is not None:
        plt.savefig(save_to_file + "_effiency.png")