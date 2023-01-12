import subprocess
import datetime
import os

class BashSubmitter:

    def __init__(self, account_id, container, runner = subprocess.run, extra_arguments=[], extra_modules=[]):
        self._run = runner
        self._container = container
        self._extra_arguments = extra_arguments

        # We do not use extra modules
        assert len(extra_modules) == 0

    def pull_container(self):
        self._container.pull()

    def __call__(self, *, inputfile, outputdir, jobname, number_of_processes,
        threads=1, walltime=datetime.timedelta(seconds=60*60)):


        outputfilename = f"{jobname}_output.txt"
        cmd = self._container(['mpiexec','-np', str(number_of_processes), 
                        'flow', inputfile, f"--threads-per-process={threads}", f'--output-dir={outputdir}', *self._extra_arguments])
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