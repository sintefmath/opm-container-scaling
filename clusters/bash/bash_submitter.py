import subprocess
import datetime
import os

class BashSubmitter:

    def __init__(self, account_id, container_name, stored_container_name, runner = subprocess.run):
        self._run = runner
        self._stored_container_name = stored_container_name
        self._container_name = container_name

    def pull_container(self):
        self._run(['singularity', 'pull', self._stored_container_name, self._container_name], check=True)

    def __call__(self, *, inputfile, outputdir, jobname, number_of_processes,
        threads=1, walltime=datetime.timedelta(seconds=60*60)):


        cwd=os.getcwd()
        outputfilename = f"{jobname}_output.txt"
        cmd = ['singularity',
                        'exec', '-B', f"{cwd}:{cwd}",  '--pwd', cwd, self._stored_container_name, 
                        'mpiexec','-np', str(number_of_processes), 
                        'flow', inputfile, f'--output-dir={outputdir}']
        try:
            with open(outputfilename, 'w') as stdoutfile:
                self._run(cmd, text=True,
                            check = True, stdout=stdoutfile, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            with open(outputfilename) as f:
                print(f"Error when running command:\n{' '.join(cmd)}")
                print("\nOutput:\n\n")
                print(f.read())
                raise e

        return outputfilename