import datetime
import click
import clusters
import utils
import datetime

@click.group()
@click.option("--inputfile", type=str, help="Input datafile (.DATA)")
@click.option("--jobname", help="Name of job")
@click.option('--number_of_processes', type=int, default=1)
@click.option('--outputdir', type=str, default='output')
@click.option('--runtime_seconds', type=int, default=60*60)
def submit_job(inputfile, outputdir, jobname, number_of_processes, runtime_seconds):
    submitter = clusters.get_submitter()
    
    submitter(inputfile=inputfile, outputdir=outputdir, jobname=jobname, 
        number_of_processes=number_of_processes, walltime=datetime.timedelta(seconds=runtime_seconds))




if __name__ == '__main__':
    submit_job.add_command(clusters.get_submitter)
    submit_job.add_command(utils.get_runner)
    submit_job()
