import subprocess
import datetime
from .base_it4i import BaseIT4I

class Barbora(BaseIT4I):

    def __init__(self, account_id, container, runner = subprocess.run):
        super().__init__(account_id, container, 36, runner=runner)