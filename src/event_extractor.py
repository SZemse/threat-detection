def extract_events(logs):

    events = []

    for log in logs:

        log = log.lower()

        if "logged in" in log:
            events.append("login_success")

        if "root" in log or "admin" in log:
            events.append("admin_access")

        if "ssh" in log:
            events.append("ssh_connection")

        if "multiple hosts" in log:
            events.append("multiple_hosts")

        if "failed login" in log:
            events.append("failed_logins")

        if "port scanning" in log:
            events.append("port_scan")

    return events