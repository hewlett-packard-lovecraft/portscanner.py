from args import parse_args
from datetime import datetime
from scanner.scanner import Scanner
import ipaddress

def main():
    args = parse_args()
    #print(args)

    verbose: bool = False
    min_port: int = 1
    max_port: int = 1024

    if args.verbose:
        verbose = True

    if args.p:
        ports = args.p.split("-")
        min_port = (int) (ports[0])
        max_port = (int) (ports[-1])

    scanner = Scanner(min_port, max_port, verbose)
    print(f'Starting portscanner.py at {datetime.now()}')

    if args.sL:
        scanner.scan_list(ipaddress.ip_network(args.sL))

    if args.sn:
        network: list[str] = list(ipaddress.ip_network(args.sn).hosts())
        scanner.set_targets(targets_str=network)
        scanner.ping_scan()
        scanner.print_scan_report()

    if args.n:
        network: list[str] = list(ipaddress.ip_network(args.sn).hosts())
        scanner.set_targets(network)

    if args.target_specification:
        scanner.set_targets(args.target_specification)
        scanner.scan_targets()
        scanner.print_scan_report()



if __name__ == "__main__":
    main()

