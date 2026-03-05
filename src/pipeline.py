from event_extractor import extract_events
from simple_reasoner import run_reasoner


def load_logs(file_path):
    with open(file_path, "r") as f:
        logs = [line.strip() for line in f.readlines()]
    return logs


def main():

    print("Neurosymbolic Threat Detection System\n")

    logs = load_logs("data/network_logs.txt")

    print("Input Logs:")
    for log in logs:
        print(log)

    events = extract_events(logs)

    print("\nExtracted Events:")
    print(events)

    threats = run_reasoner(events)

    print("\nFinal Threats:", threats)


if __name__ == "__main__":
    main()