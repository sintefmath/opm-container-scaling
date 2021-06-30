import argparse
import datetime


def make_time(time_as_string):
    time = datetime.datetime.strptime(time_as_string,"%H:%M:%S")
    return datetime.timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

def add_walltime_argument(parser: argparse.ArgumentParser):
    parser.add_argument('--walltime', type=make_time, default="01:00:00")
