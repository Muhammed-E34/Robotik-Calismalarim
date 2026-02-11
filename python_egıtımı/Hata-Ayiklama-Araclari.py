import time
import sys

def system_health_check():
    """
    Simulates a system diagnostic check.
    Replacing visual output test patterns with standard logging.
    """
    print("[DIAGNOSTIC] Initiating Core System Check...")
    toolbar_width = 40

    # Setup progress bar (Loading effect)
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    for i in range(toolbar_width):
        time.sleep(0.05) # do real work here
        # update the bar
        sys.stdout.write("#")
        sys.stdout.flush()

    sys.stdout.write("]\n")
    print("[SUCCESS] All systems operational. No legacy artifacts found.")

if __name__ == "__main__":
    system_health_check()