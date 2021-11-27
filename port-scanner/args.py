import argparse, sys
from _version import __version__

def parse_args():
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description='Port scanner in python.'
    )

    parser.add_argument(
        '-p',
        type=str,
        metavar="ports",
        help='Only scan specified range separated by hyphen or specified port (defaults to 1-1024)',
        action='store'
    )

    """
    parser.add_argument(
        '-Pn',
        help='disable ping scan',
        action='store_true'
    )
    """

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
    conflicting = parser.add_mutually_exclusive_group()

    conflicting.add_argument(
        '-sL',
        type=str,
        metavar="network",
        help="scan list - list targets to scan from a network"
    )

    conflicting.add_argument(
        '-sn',
        type=str,
        metavar="network",
        help="ping scan - list hosts online on a network, disable port scan"
    )

    conflicting.add_argument(
        '-n',
        type=str,
        metavar="network",
        help="ping scan - locate and scan hosts online on a network"
    )

    conflicting.add_argument(
        'target_specification',
        nargs='*',
        default=[],
        action='store',
        help="Specify a target or targets using IP address or hostname",
    )

    return parser.parse_args((None if sys.argv[1:] else ['-h'])) # magic oneliner that prints help if no args are passed
