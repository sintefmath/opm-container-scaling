import re
import os

def get_runtime(filename, time_key='Total time', per_quantity=None):
    runtime = None

    if  per_quantity is not None:
        iterations =  None
    else:
        iterations = 1
    with open(filename) as f:
        for line in f:
            if match := re.search(rf'{time_key} \(seconds\):\s+(\d+.\d+)', line):
                runtime = float(match.group(1))
            if per_quantity is not None:
                if match := re.search(rf'{per_quantity}:\s+(\d+)', line):
                    iterations = float(match.group(1))
        if iterations is None:
            raise Exception(f"\"{per_quantity}\" not found in {filename}.")
        if  runtime is None:
            raise Exception(f"\"{time_key}\" not found in {filename}.")
        return runtime / iterations
       
        
def get_runtimes(configuration, skip_missing=False, time_key='Total time', per_quantity=None):
    runtimes = []
    for filename in configuration['output_filenames']:
        if os.path.exists(filename):
            try:
                runtimes.append(get_runtime(filename,  time_key=time_key,  per_quantity=per_quantity))
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
    