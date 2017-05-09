import argparse
#import brightnessmonitorclient
#from brightnessmonitorclient import __version__
from brightnessmonitorclient.raspberry.main import start


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('BrightnessMonitorClient')
    #version = '%(prog)s ' + __version__
    #parser.add_argument('--version', '-v', action='version', version=version)
    return parser

def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    # start raspberry.main:start
    start()


if __name__ == '__main__':
    main()