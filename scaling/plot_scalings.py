from .get_runtime import get_runtimes
import json
import matplotlib.pyplot as plt
import numpy as np


def plot_scalings(configuration_files, skip_missing=True, save_to_file=None, show=True):
    
    
    symbols = ['-o', '-*', '-x']
    for n, configuration_file in enumerate(configuration_files):
        with open(configuration_file) as f:
            configuration = json.load(f)
    
        runtimes = get_runtimes(configuration)

        number_of_processes_list = np.array(list(map(int, configuration['number_of_processes_list'])), dtype=np.float64)
        plt.loglog(number_of_processes_list,
                   runtimes, symbols[n%len(symbols)], label=configuration_file)
        
    plt.loglog(number_of_processes_list, 
               runtimes[0] * number_of_processes_list[0] * number_of_processes_list**(-1),
               '--', label='Ideal')
    
    plt.ylabel('Runtime [s]')
    plt.xlabel('Number of processes')
    plt.grid(True)
    plt.xscale('log', base=2)
    plt.yscale('log', base=2)
    plt.legend()
    if show:
        plt.show()
        
    if save_to_file is not None:
        plt.savefig(save_to_file)