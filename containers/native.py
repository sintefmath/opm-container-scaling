import os


class Native:
    def __init__(self, runner, container_name, stored_container_name):
        pass
        
    def __call__(self, cmd, binds=[[os.getcwd(), os.getcwd()]], workdir=os.getcwd()):
        return cmd
    
    def pull(self):
        pass