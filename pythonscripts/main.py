# main.py
from netmiko import ConnectHandler
import argparse

def main():
    parser = argparse.ArgumentParser(description="Netmiko Command Service")
    parser.add_argument('--command', required=True, help="Command to run")
    parser.add_argument('--host', required=True, help="Host to connect to")
    args = parser.parse_args()
    # YOUR EXECUTION CODE GOES BELOW THIS LINE    

    cisco1 = {
        "device_type": "cisco_ios",
        "host": args.host
    }
    with ConnectHandler(**cisco1) as net_connect:
        output = net_connect.send_command(args.command)

    print(output)

if __name__ == "__main__":
    main()