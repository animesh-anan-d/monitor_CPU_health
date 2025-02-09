import psutil
import time
import sys

# Set the limit for CPU usage
CPU_THRESHOLD = 80  # If CPU usage goes above this, we show a warning
MONITOR_INTERVAL = 1  # Wait time (in seconds) before checking again

def get_cpu_usage():
    """
    Get the current CPU usage in percentage.
    Returns:
        float: How much CPU is being used right now.
    """
    return psutil.cpu_percent(interval=MONITOR_INTERVAL)

def monitor_cpu():
    """
    Keep checking the CPU usage and warn if it gets too high.
    This runs forever until the user stops it.
    """
    print("Checking CPU usage... Press Ctrl+C to stop.\n")

    try:
        while True:
            cpu_usage = get_cpu_usage()  # Check CPU usage
            if cpu_usage > CPU_THRESHOLD:
                # Show a warning if CPU usage is too high
                print(f"🚨 Warning! CPU usage is too high: {cpu_usage}%")
            
            # Wait before checking again
            time.sleep(MONITOR_INTERVAL)

    except KeyboardInterrupt:
        # If the user stops the program, show a message
        print("\nStopped by user. Exiting...")
        sys.exit(0)

    except Exception as e:
        # If something goes wrong, show an error message
        print(f"⚠️ Oops! Something went wrong: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    monitor_cpu()
