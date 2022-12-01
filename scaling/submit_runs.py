import json
import argparse


def add_arguments_submit_runs(parser: argparse.ArgumentParser):
    parser.add_argument("--inputfile", type=str, help="Input datafile (.DATA)")
    parser.add_argument("--jobname_base", required=True, help="Basename of job (will be {jobname_base}_{num_procs})")
    parser.add_argument('--number_of_processes_list', type=int, nargs="+", required=True,
                        help="List of number of processes to run.")
    parser.add_argument('--outputdir_base', type=str, default='output')


def submit_runs(submitter, *, inputfile, outputdir_base, jobname_base, number_of_processes_list,
                walltime, **ignored_kwargs):
    output_filenames = []
    for number_of_processes in number_of_processes_list:
        outputdir = f"{outputdir_base}_{number_of_processes}"
        jobname = f"{jobname_base}_{number_of_processes}"
        output_filename = submitter(inputfile=inputfile, outputdir=outputdir, jobname=jobname,
                                    number_of_processes=number_of_processes, walltime=walltime)

        output_filenames.append(output_filename)

    with open(f"{jobname_base}.json", "w") as f:
        json.dump({"output_filenames": output_filenames, "number_of_processes_list": number_of_processes_list}, f,
                  indent=4)
