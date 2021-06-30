from .docker import Docker
from .singularity import Singularity
from .native import Native

def get_container(container_type, runner, container_name, stored_container_name):
    container_types = {
        "docker" : Docker,
        "native" : Native,
        "singularity" : Singularity
    }
    
    if container_type  not in container_types.keys():
        raise Exception(f"Unknown container type {container_type}.")
    
    return container_types[container_type](runner, container_name, stored_container_name)