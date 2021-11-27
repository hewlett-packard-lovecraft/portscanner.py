from .host import Host
from sys import platform
import sys, time, datetime, ipaddress

class Scanner:
    targets: list[Host] = []
    verbose: bool = False
    min_port: int = 1
    max_port: int = 1024

    def __init__(self, min_port: int, max_port: int, _verbose: bool):
        self.min_port = min_port
        self.max_port = max_port
        self.verbose = _verbose

    def set_targets(self, targets_str: list[str]):
        targets_new: list[Host] = []

        for target in targets_str:
            targets_new.append(Host(target))

        self.targets = targets_new

    def scan_targets(self): # multithread this
        for target in self.targets:
            target.scan_ports(self.min_port, self.max_port, self.verbose)

    def scan_list(self, network: ipaddress.IPv4Network):
        for host in network.hosts(): # print list of available addresses in a network
            print(host)

        return network.hosts()

    def ping_scan(self): # multithread this also
        hosts_up: list[Host] = []

        if platform == 'windows':
            print(f'Ping scan on platform {platform} is currently not supported at this time')
            sys.exit()

        if self.verbose:
            print(f"Initiating ping scan at {datetime.datetime.now()}")

        hosts_down = 0
        start_time = time.perf_counter()

        for target in self.targets:
            if target.ping():
                hosts_up.append(target)
            else:
                hosts_down += 1

        end_time = time.perf_counter()

        if self.verbose:
            print(f"Ping scan completed at {datetime.datetime.now}, {end_time - start_time}s elapsed [{hosts_down} hosts down]")

        return hosts_up

    def scan_network(self, network: ipaddress.IPv4Network): # look at how nmap does it and come up with a verbose option soonish
        self.ping_scan()
        self.scan_targets()

    def print_scan_report(self):
        for target in self.targets:
            target.scan_report()

