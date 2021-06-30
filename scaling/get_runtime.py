import re


def get_runtime(filename):
    with open(filename) as f:
        for line in f:
            if match := re.search(r'Total time \(seconds\):\s+(\d+.\d+)', line):
                return float(match.group(1))
        else:
            raise Exception(f"Runtime not found in {filename}.")
        
def get_runtimes(configuration):
    runtimes = []
    for filename in configuration['output_filenames']:
        runtimes.append(get_runtime(filename))
    
    return runtimes
    