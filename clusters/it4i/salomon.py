import subprocess
import datetime
from .base_it4i import BaseIT4I

class Salomon(BaseIT4I):

    def __init__(self, account_id, container, runner = subprocess.run):
        super().__init__(account_id, container, 24, runner=runner)