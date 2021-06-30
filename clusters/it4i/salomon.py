import subprocess
import datetime

class Salomon:

    def __init__(self, account_id, container_name, stored_container_name, runner = subprocess.run):
        self._account_id = account_id
        self._run = runner
        self._container_name = container_name
        self._stored_container_name = stored_container_name

    def pull_container(self):
        self._run(["ml", "Singularity"], check=True)
        self._run(["singularity", "pull", self._stored_container_nameo, 
            self._container_name], check=True)
        
    def _load_modules_script(self):
        modulenames =  ["Singularity", "OpenMPI/2.1.1-GCC-7.3.0-2.30"]
        return "\n".join(f"ml {modulename}" for modulename in modulenames)

    def __call__(self, *, inputfile, outputdir, jobname, number_of_processes,
        threads=1, runtime=datetime.timedelta(seconds=60*60)):


        walltime = str(runtime)
        procs_per_node = 24

        # TODO Give a nice error message explaining the problem (or allow nodes that are not filled up)
        assert number_of_processes % procs_per_node == 0
        # TODO add support for threads
        assert threads == 1
        number_of_nodes = number_of_processes // procs_per_node

        submission_script = f"""
        #!/bin/bash
        {self._load_modules_script()}

        mpiexec -np {number_of_processes} singularity exec -B $(pwd):$(pwd) --pwd $(pwd) flow {inputfile} --output-dir={outputdir}"
        """

        output = self._run(['qsub', '-N', jobname, 
            '-A', self._account_id,
            '-l', f'select={number_of_nodes}:ncpus={procs_per_node}:mpiprocs={procs_per_node},walltime={walltime}'
            ], check = True, text=True, 
            input=submission_script, encoding='ascii', capture_output=True)

        jobid = output.stdout
        return f"{jobname}.{jobid}"