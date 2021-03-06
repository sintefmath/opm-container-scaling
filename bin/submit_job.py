import datetime
import clusters
import utils
import datetime
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        Submits the job to the cluster queue.
    """)
    parser.add_argument("--inputfile", type=str, help="Input datafile (.DATA)")
    parser.add_argument("--jobname", required=True, help="Name of job")
    parser.add_argument('--number_of_processes', type=int, default=1)
    parser.add_argument('--outputdir', type=str, default='output')
    parser.add_argument('--do_not_pull_container', action='store_true', help="Pull the container.")
    utils.add_walltime_argument(parser)

    clusters.add_arguments_get_submitter(parser)
    args = parser.parse_args()
    submitter = clusters.get_submitter(**vars(args))
    if not args.do_not_pull_container:
        submitter.pull_container()
    
    submitter(inputfile=args.inputfile, outputdir=args.outputdir, jobname=args.jobname, 
        number_of_processes=args.number_of_processes, walltime=args.walltime)

