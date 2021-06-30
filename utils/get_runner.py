import click
import subprocess

def dry_run(cmd_list, check = False, text=False, input=None, encoding=None,
    capture_output=False):
    print("#"*80)
    if input is not None:
        print(f"Running with the following input:\n{input}\n\n")
    
    print(f"Would run: {' '.join(cmd_list)}\n")
    print("#"*80)

    if capture_output:
        return subprocess.CompletedProcess(args=cmd_list, returncode=0,
            stdout='fake', stderr='fake')



@click.command()
@click.option("--dry_run", is_flag=True)
def get_runner(dry_run):
    if dry_run:
        return dry_run
    else:
        return subprocess.run
