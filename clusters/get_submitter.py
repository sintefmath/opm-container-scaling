import utils
import containers
import argparse
from . import it4i
from . import bash

def _get_cluster_name():
    import socket
    fullname = socket.getfqdn()
    
    # for IT4I/Salomon: 'login1.head.smc.salomon.it4i.cz'
    if fullname.endswith('salomon.it4i.cz'):
        return 'salomon.it4i.cz'
    elif fullname.endswith('barbora.it4i.cz'):
        return 'barbora.it4i.cz'
    elif fullname.endswith('karolina.it4i.cz'):
        return 'karolina.it4i.cz'
    else:
        raise Exception(f"Unknown clustername {fullname}.")

def add_arguments_get_submitter(parser: argparse.ArgumentParser):
    parser.add_argument('--container_type', type=str, default='singularity', help="Name of the container type (native, docker, singularity)")
    parser.add_argument("--container_name", type=str, default="docker://openporousmedia/opmreleases", 
        help="Name of the container to pull.")
    parser.add_argument("--stored_container_name", default="opmreleases_latest.sif", 
        help="Name of the container locally on cluster.")
    parser.add_argument("--cluster_name", default="auto", help="Name of the cluster")

    parser.add_argument("--account_id", required=True, type=str, help="Account ID for submission")

    parser.add_argument('--dry_run', action='store_true', 
                        help="Only print the commands to be run, do not actually run it.")
    
def get_submitter(*, container_type, container_name, stored_container_name, account_id, 
     cluster_name, dry_run, **ignored_kw_args):
    if cluster_name.lower() == 'auto':
        cluster_name = _get_cluster_name()

    
    runner = utils.get_runner(dry_run)
    container = containers.get_container(container_type, runner, container_name, stored_container_name)    
    clusters = {
        'salomon.it4i.cz' : it4i.Salomon,
        'barbora.it4i.cz' : it4i.Barbora,
        'karolina.it4i.cz': it4i.Karolina,
        'bash' : bash.BashSubmitter
    }
    if cluster_name in clusters.keys():
        return clusters[cluster_name.lower()](account_id, container, runner)
    else:
        raise Exception(f"Unknown cluster {cluster_name}.")


