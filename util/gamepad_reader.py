import sys
import json
from inputs import devices

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    device_path = sys.argv[1]

    dev = next((d for d in devices.all_devices if d._device_path == device_path), None)
    if dev is None:
        sys.exit(1)

    # force unbuffered stdout
    sys.stdout.reconfigure(line_buffering=True)

    try:
        while True:
            events = dev.read()          # blocking read, returns list
            for ev in events:
                sys.stdout.write(json.dumps({
                    "ev_type": ev.ev_type,
                    "code": ev.code,
                    "state": ev.state
                }) + "\n")
                sys.stdout.flush()
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()