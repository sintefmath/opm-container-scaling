import subprocess
import datetime
from .base_it4i import BaseIT4I

class Barbora(BaseIT4I):

    def __init__(self, account_id, container, runner = subprocess.run, extra_arguments=[]):
        super().__init__(account_id, container, 36, runner=runner, extra_arguments=extra_arguments)