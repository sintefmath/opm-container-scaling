import click
import utils

def _get_cluster_name():
    import socket
    fullname = socket.getfqdn()
    
    # for IT4I/Salomon: 'login1.head.smc.salomon.it4i.cz'
    if fullname.endswith('salomon.it4i.cz'):
        return 'salomon.it4i.cz'
    else:
        raise Exception(f"Unknown clustername {fullname}.")

@click.command()
@click.option("--container_name", default="docker://openporousmedia/opmreleases", 
    help="Name of the container to pull.")
@click.option("--stored_container_name", default="docker://openporousmedia/opmreleases", 
    help="Name of the container locally on cluster.")
@click.option("--cluster_name", default="auto", help="Name of the cluster")
def get_submitter(container_name, stored_container_name, inputfile, account_id, 
    output_folder, cluster_name):
    if cluster_name.lower() == 'auto':
        cluster_name = _get_cluster_name()
    
    runner = utils.get_runner()
    if cluster_name == 'salomon.it4i.cz':
        return it4i.Salomon(account_id, container_name, stored_container_name, runner)
    else:
        raise Exception(f"Unknown cluster {cluster_name}.")


