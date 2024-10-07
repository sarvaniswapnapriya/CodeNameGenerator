import datetime

def logger(message):
    """Simple logger with timestamps."""
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{time}] {message}")
