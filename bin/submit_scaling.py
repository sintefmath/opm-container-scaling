import datetime
import clusters
import utils
import datetime
import argparse
import scaling

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        Submits the job to the cluster queue.
    """)
    parser.add_argument('--do_not_pull_container', action='store_true', help="Pull the container.")
    scaling.add_arguments_submit_runs(parser)
    utils.add_walltime_argument(parser)

    clusters.add_arguments_get_submitter(parser)
    args = parser.parse_args()
    submitter = clusters.get_submitter(**vars(args))
    if not args.do_not_pull_container:
        submitter.pull_container()
    
    scaling.submit_runs(submitter, **vars(args))