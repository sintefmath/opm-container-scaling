# opm-container-scaling
Various scripts for running scaling tests for OPM within a container (docker and singularity).

## Example: Running Norne with comparison between Native, Docker and Singularity natively

All commands are assumed to be run from the root of this repository. First clone the ```opm-data``` repository:

```bash
git clone https://github.com/OPM/opm-data
```

We assume the current repository is in your ```PYTHONPATH```, if not, add it:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

Then run a simple scaling run on 1 to 6 processes:

First on Singularity:


```
python bin/submit_scaling.py \
     --inputfile opm-data/norne/NORNE_ATW2013.DATA \
     --account_id 1234 --cluster_name bash \
     --number_of_processes_list 1 2 3 4 5 6 \
     --jobname_base norne_singularity \
     --container_type singularity \
     --outputdir_base output_singularity
```

then on Docker


```
python bin/submit_scaling.py \
     --inputfile opm-data/norne/NORNE_ATW2013.DATA \
     --account_id 1234 --cluster_name bash \
     --number_of_processes_list 1 2 3 4 5 6 \
     --jobname_base norne_docker --container_type docker \
     --outputdir_base output_docker \
     --do_not_pull_container \
     --container_name openporousmedia/opmreleases
```

and finally on native (assumes ```flow``` is in your ```PATH```):

```
python bin/submit_scaling.py --inputfile opm-data/norne/NORNE_ATW2013.DATA \
     --account_id 1234 --cluster_name bash --number_of_processes_list 1 2 3 4 5 6 \
     --jobname_base norne_native \
     --container_type native \
     --outputdir_base output_native
```

You should now have three files named 

```
norne_docker.json 
norne_native.json
norne_singularity.json
```

you can plot the results with

```
python bin/plot_scaling.py \
    --configuration_files \
        norne_docker.json norne_docker.json norne_native.json \
    --show
```


