import click
import subprocess

def dry_run_function(cmd_list, check = False, text=False, input=None, encoding=None,
    capture_output=False, stdout=None, stderr=None):
    print("#"*80)
    if input is not None:
        print(f"Running with the following input:\n{'-'*80}\n{input}\n{'-'*80}\n\n")
    
    print(f"Would run:\n\t{' '.join(map(str, cmd_list))}\n")
    print("#"*80)

    if capture_output:
        return subprocess.CompletedProcess(args=cmd_list, returncode=0,
            stdout='fake', stderr='fake')


def get_runner(dry_run):
    if dry_run:
        return dry_run_function
    else:
        return subprocess.run
