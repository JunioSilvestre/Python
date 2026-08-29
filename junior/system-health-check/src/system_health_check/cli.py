import socket


def main() -> None:
    hostname = socket.gethostname()
    print(f"System Health Check")
    print(f"Hostname: {hostname}")


if __name__ == "__main__":
    main()