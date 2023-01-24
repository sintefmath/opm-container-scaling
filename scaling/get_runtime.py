import re
import os

def get_runtime(filename):

    with open(filename) as f:
        for line in f:
            if match := re.search(r'Total time \(seconds\):\s+(\d+.\d+)', line):
                return float(match.group(1))
        else:
            raise Exception(f"Runtime not found in {filename}.")
        
def get_runtimes(configuration, skip_missing=False):
    runtimes = []
    for filename in configuration['output_filenames']:
        if os.path.exists(filename):
            try:
                runtimes.append(get_runtime(filename))
            except Exception as e:
                if skip_missing:
                    runtimes.append(-1)
                else:
                    raise e
        else:
            if skip_missing:
                runtimes.append(-1)
            else:
                raise Exception(f"File not found: {filename}")
    
    return runtimes
    