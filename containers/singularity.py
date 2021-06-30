import os


class Singularity:
    def __init__(self, runner, container_name, stored_container_name):
        self.container_name = container_name
        self.stored_container_name = stored_container_name
        self._run = runner
        
    def __call__(self, cmd, binds=[[os.getcwd(), os.getcwd()]], workdir=os.getcwd()):
        
        commandlist = ['singularity', 'exec']
        for bind in binds:
            commandlist.extend(['-B', f"{bind[0]}:{bind[1]}"])
        
        commandlist.extend(['--pwd', workdir])
        commandlist.append(self.stored_container_name)
        commandlist.extend(cmd)

        return commandlist
    
    def pull(self):
        self._run(['singularity', 'pull', self.stored_container_name, self.container_name], check=True)         
            
            