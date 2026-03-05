def run_reasoner(events):

    print("\nRunning symbolic reasoning...\n")

    threats = []

    if "login_success" in events and "admin_access" in events:
        threats.append("privilege_escalation")

    if "ssh_connection" in events and "multiple_hosts" in events:
        threats.append("lateral_movement")

    if "port_scan" in events and "failed_logins" in events:
        threats.append("brute_force_attack")

    print("Detected threats:\n")

    for t in threats:
        print("Threat detected:", t)

    return threats