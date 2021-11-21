import argparse
from _version import __version__

def parse_args():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Port scanner in python.'
    )

    parser.add_argument(
        'target_specification',
        nargs='+',
        help="Specify a target or targets using IP address or hostname",
    )

    parser.add_argument(
        '-v',
        '--verbose',
        help='Increase output verbosity',
        action='store_true'
    )

    parser.add_argument(
        '-V',
        '--version',
        help="Print version number",
        action='version',
        version='%(prog)s ' + __version__
    )

    return parser.parse_args()
