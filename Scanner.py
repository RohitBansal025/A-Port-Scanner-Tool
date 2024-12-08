import sys
import socket
import threading
from datetime import datetime

# Define your target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

# List of common ports to scan first
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 587, 993, 995]

# List to keep track of open ports
open_ports = []

# Lock for thread-safe access to the open_ports list
lock = threading.Lock()

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        with lock:
            open_ports.append(port)
            print(f"Port {port} is open")
    s.close()

def thread_scan(ports):
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

try:
    # Scan common ports first
    print("Scanning common ports...")
    thread_scan(common_ports)

    # Scan the rest of the ports
    start_port = int(input("Enter start port for full scan: "))
    end_port = int(input("Enter end port for full scan: "))
    all_ports = list(range(start_port, end_port + 1))

    # Remove common ports from the full port list to avoid re-scanning
    all_ports = [port for port in all_ports if port not in common_ports]

    print("Scanning all ports...")
    thread_scan(all_ports)

    print("-" * 50)
    print(f"Scanning Completed: {str(datetime.now())}")
    print("-" * 50)
    print(f"Open Ports: {open_ports}")

except KeyboardInterrupt:
    print("\nExiting program")
except socket.gaierror:
    print("Hostname could not be resolved")
except socket.error:
    print("Could not connect to server")
except ValueError:
    print("Invalid port number")
finally:
    sys.exit()
