import argparse
import datetime
import re
class Walltime:
    def __init__(self, *, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'


def make_time(time_as_string):
    match = re.search(r'(\d+):(\d+):(\d+)', time_as_string)
    if not match:
        raise ValueError(f"Unrecognized walltime format {time_as_string}, expected 'HH:MM:SS'")
    return Walltime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
    

def add_walltime_argument(parser: argparse.ArgumentParser):
    parser.add_argument('--walltime', type=make_time, default="01:00:00")
