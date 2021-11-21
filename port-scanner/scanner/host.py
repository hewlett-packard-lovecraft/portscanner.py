import socket
import sys
import time, datetime

class Host(object):
    ip: str = ""
    fqdn: str = ""
    open_ports: list[tuple[int, str, str, str]] = [] # (port, protocol, state, service)
    scan_time: float = 0.0

    def __init__(self, _ip: str):
        self.ip = _ip

    def tcp_scan(self, min_port: int, max_port: int, verbose: bool): # scan range of ports
        open_ports: list[tuple[int, str, str, str]] = []
        try:
            for port in range(min_port, max_port + 1):
                port_open = False
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                if not sock.connect_ex((self.ip, port)):
                    port_open = True
                    serv = socket.getservbyport(port)
                    open_ports.append((port, "tcp", "open", serv))

                if verbose and port_open:
                    print(f"Discovered open port {port} on {self.ip}")

        except socket.gaierror:
            print(f'Hostname could not be resolved for target {self.ip}. Exiting')
            sys.exit()

        except socket.error:
            print(f"Couldn't connect to target {self.ip}")
            sys.exit()
        finally:
            return open_ports

    def scan_ports(self, min_port: int, max_port: int, verbose: bool): # scan range of ports
        self.fqdn = socket.getfqdn(self.ip)

        if verbose:
            print(f"Initiating scan at {datetime.datetime.now()} on target {self.fqdn} ({self.ip})")

        start = time.perf_counter()

        open_ports = self.tcp_scan(min_port, max_port, verbose)

        end = time.perf_counter()

        self.scan_time = (float) (end - start)

        if verbose:
            print(f"Completed TCP scan at {datetime.datetime.now()}, {self.scan_time}s elapsed")

        self.open_ports = open_ports


    def scan_report(self):
        print(f"Scan report for {self.fqdn} ({self.ip})")

        print("PORT    STATE SERVICE")
        for port in self.open_ports:
            port_and_proto = f"{port[0]}/{port[1]}"
            state = port[2]
            serv = port[3]

            print(f'{port_and_proto:<7} {state:<5} {serv:<8}')
