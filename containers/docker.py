import os


class Docker:
    def __init__(self, runner, container_name, stored_container_name):
        self.container_name = container_name
        self._run = runner
        
    def __call__(self,cmd, binds=[[os.getcwd(), os.getcwd()]], workdir=os.getcwd()):
        
        commandlist = ['docker', 'run']
        for bind in binds:
            commandlist.extend(['-v', f"{bind[0]}:{bind[1]}"])
        
        commandlist.extend(['-w', workdir])
        commandlist.append(self.container_name)
        commandlist.extend(cmd)

        return commandlist
    
    def pull(self):
        self._run(['docker', 'pull', self.container_name], check=True)         
            
            