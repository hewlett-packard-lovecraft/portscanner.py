from args import parse_args
from scanner.host import Host

def main():
    args = parse_args()

    verbose: bool = args.verbose

    host:  Host = Host(args.target_specification[0])

    host.scan_ports(1, 1024, verbose)
    host.scan_report()

if __name__ == "__main__":
    main()

