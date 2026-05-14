import os

LOG_FILE = "/var/log/syslog"

CRITICAL_PATTERNS = {
    "error": "Potential system error detected",
    "failed": "Failure event detected",
    "panic": "Kernel panic detected",
    "segfault": "Segmentation fault detected",
    "critical": "Critical event detected",
}


def analyze_log():
    print("AI Log Analyzer")
    print("-" * 40)

    if not os.path.exists(LOG_FILE):
        print("Log file not found.")
        return

    try:
        with open(LOG_FILE, "r", errors="ignore") as file:
            lines = file.readlines()

        for line in lines[-100:]:
            lower_line = line.lower()

            for keyword, message in CRITICAL_PATTERNS.items():
                if keyword in lower_line:
                    print(f"[!] {message}")
                    print(f"    Log: {line.strip()}")
                    print()

    except PermissionError:
        print("Permission denied while reading logs.")


if __name__ == "__main__":
    analyze_log()
