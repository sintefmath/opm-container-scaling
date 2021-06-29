# The Salomon and Barbora clusters on IT4I

Please note that these instructions may be outdated by the time you read this. For updated instructions, 
please consult the [IT4I support pages](https://docs.it4i.cz/). These instructions are still under development, and may contain both errors and suboptimal solutions. If you notice room for improvement, please let us know!

## Rudimentary sandboxing
It is a good idea to run all the commands below from a new, empty folder in your home directory

```bash
cd 
mkdir opm_singularity
cd opm_singularity
```

## Getting the container
First you will need to load the Singularity module:

```
ml Singularity
```

then you can pull the ```openporousmedia/opmreleases``` container

```
singularity pull docker://openporousmedia/opmreleases
```

To verify that everything worked, run

```
singularity exec opmreleases_latest.sif which flow
```

which should output (note that the ```INFO``` part might not appear)

```
INFO:    Could not find any nv files on this host!
/usr/bin/flow
```

## Running the Norne field case

First we will need to obtain the simulation data

```bash
git clone https://github.com/OPM/opm-data.git
```

Now we need to check the MPI version of the container to load the appropriate module

```bash
singularity exec opmreleases_latest.sif mpirun --version
```

this should output something like

```
INFO:    Could not find any nv files on this host!
mpirun (Open MPI) 2.1.1

Report bugs to http://www.open-mpi.org/community/help/
```

At the time of writing, the closest matching module on IT4I is ```OpenMPI/2.1.1-GCC-7.3.0-2.30``` but this might change in the future. Use ```ml av``` to get a list of all available modules (ml also supports autocomplete with TAB). 

Create a new file called ```run_norne.sh``` with the following content

```bash
#!/bin/bash
ml Singularity
ml OpenMPI/2.1.1-GCC-7.3.0-2.30
mpiexec -np 48 singularity exec --pwd $(pwd) -B $(pwd):$(pwd) opmreleases_latest.sif flow opm-data/norne/NORNE_ATW2013.DATA --output-dir=output --threads-per-process=1
```

then make this file executable

```
chmod +x run_norne.sh
```

and submit

```bash
qsub -A <project ID> -l select=2:ncpus=24:mpiprocs=24,walltime=01:00:00 ./run_norne.sh
```

You can monitor your jobs with

```
qstat -a -u <your username>
```

Once the job has finished you should see two files named ```run_norne.sh.o<jobid>``` and ```run_norne.sh.e<jobid>```, where the former contains STDOUT and the latter STDIN. The simulation output will be located in the ```output``` folder.