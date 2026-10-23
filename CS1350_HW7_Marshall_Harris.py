
def split_logs(machines):
    counts = {}

    with open("info.log", "w") as info_file, \
         open("warning.log", "w") as warning_file, \
         open("error.log", "w") as error_file:

        for machine, filename in machines.items():
            counts[machine] = {
                "INFO": 0,
                "WARNING": 0,
                "ERROR": 0
            }

            with open(filename, "r") as log_file:
                for line in log_file:
                    line = line.strip()

                    if line == "":
                        continue

                    if "[INFO]" in line:
                        info_file.write(machine + " | " + line + "\n")
                        counts[machine]["INFO"] += 1

                    elif "[WARNING]" in line:
                        warning_file.write(machine + " | " + line + "\n")
                        counts[machine]["WARNING"] += 1

                    elif "[ERROR]" in line:
                        error_file.write(machine + " | " + line + "\n")
                        counts[machine]["ERROR"] += 1

    return counts


def print_report(counts, error_file="error.log"):
    total_entries = 0
    total_info = 0
    total_warning = 0
    total_error = 0

    print("SECURITY LOG REPORT")
    print("=" * 40)

    for machine, levels in counts.items():
        info = levels["INFO"]
        warning = levels["WARNING"]
        error = levels["ERROR"]

        entries = info + warning + error

        total_entries += entries
        total_info += info
        total_warning += warning
        total_error += error

        if error >= 2:
            status = "CRITICAL"
        elif error >= 1 or warning >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"

        print(
            f"{machine}: {entries} entries | INFO {info} "
            f"| WARNING {warning} | ERROR {error} | Status: {status}"
        )

    print("-" * 40)
    print(
        f"Total: {total_entries} entries | INFO {total_info} "
        f"| WARNING {total_warning} | ERROR {total_error}"
    )

    print("Errors (see error.log):")

    with open(error_file, "r") as file:
        for line in file:
            print("  " + line.rstrip())


# Test code
with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({
    "server_a": "server_a.log",
    "server_b": "server_b.log"
})

print(counts)

with open("warning.log", "r") as f:
    print(f.read())

print_report(counts)





import json
import pickle
import os


def load_incidents(csv_file):
    incidents = []

    with open(csv_file, "r") as file:
        next(file, None)  # Skip the header

        for line in file:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(",")

            incident = {
                "id": int(parts[0]),
                "machine": parts[1],
                "severity": parts[2],
                "description": parts[3]
            }

            incidents.append(incident)

    return incidents


def save_summary(incidents, json_file):
    summary = {
        "total": len(incidents),
        "by_machine": {},
        "by_severity": {},
        "high_ids": []
    }

    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]

        if machine not in summary["by_machine"]:
            summary["by_machine"][machine] = 0

        summary["by_machine"][machine] += 1

        if severity not in summary["by_severity"]:
            summary["by_severity"][severity] = 0

        summary["by_severity"][severity] += 1

        if severity == "high":
            summary["high_ids"].append(incident["id"])

    with open(json_file, "w") as file:
        json.dump(summary, file, indent=2)

    return summary


def archive(incidents, folder):
    os.makedirs(folder, exist_ok=True)

    pickle_path = os.path.join(folder, "incidents.pkl")

    with open(pickle_path, "wb") as file:
        pickle.dump(incidents, file)

    machines = {}

    for incident in incidents:
        machine = incident["machine"]

        if machine not in machines:
            machines[machine] = []

        machines[machine].append(incident)

    for machine, machine_incidents in machines.items():
        json_path = os.path.join(folder, machine + ".json")

        with open(json_path, "w") as file:
            json.dump(machine_incidents, file, indent=2)

    return sorted(os.listdir(folder))


def load_archive(folder):
    pickle_path = os.path.join(folder, "incidents.pkl")

    with open(pickle_path, "rb") as file:
        incidents = pickle.load(file)

    return incidents


# Test code
with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")
print(len(incidents))
print(incidents[0])

summary = save_summary(incidents, "summary.json")
print(summary)

with open("summary.json", "r") as f:
    print(json.load(f) == summary)

print(archive(incidents, "archive"))

with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])

restored = load_archive("archive")
print(restored == incidents)





import os
import shutil


def organize(folder):
    categories = {
        "logs": [],
        "data": [],
        "pickles": [],
        "other": []
    }

    for name in os.listdir(folder):
        path = os.path.join(folder, name)

        # Only move files directly inside the folder
        if os.path.isfile(path):
            extension = os.path.splitext(name)[1]

            if extension == ".log":
                category = "logs"
            elif extension in [".csv", ".json"]:
                category = "data"
            elif extension == ".pkl":
                category = "pickles"
            else:
                category = "other"

            destination_folder = os.path.join(folder, category)
            os.makedirs(destination_folder, exist_ok=True)

            destination_path = os.path.join(destination_folder, name)
            shutil.move(path, destination_path)

            categories[category].append(name)

    for category in categories:
        categories[category].sort()

    return categories


def create_backup(source_dir, backup_root, label):
    os.makedirs(backup_root, exist_ok=True)

    backup_name = "backup_" + label
    backup_path = os.path.join(backup_root, backup_name)

    shutil.copytree(source_dir, backup_path)

    return backup_path


def verify_backup(source_dir, backup_dir):
    for root, folders, files in os.walk(source_dir):
        for name in files:
            source_path = os.path.join(root, name)

            relative_path = os.path.relpath(source_path, source_dir)
            backup_path = os.path.join(backup_dir, relative_path)

            if not os.path.isfile(backup_path):
                return False

            if os.path.getsize(source_path) != os.path.getsize(backup_path):
                return False

    return True


def cleanup_old_backups(backup_root, keep):
    backup_names = []

    for name in os.listdir(backup_root):
        path = os.path.join(backup_root, name)

        if name.startswith("backup_") and os.path.isdir(path):
            backup_names.append(name)

    backup_names.sort()

    if keep < 0:
        keep = 0

    if keep == 0:
        old_backups = backup_names
    else:
        old_backups = backup_names[:-keep]

    deleted = []

    for name in old_backups:
        path = os.path.join(backup_root, name)
        print("Deleting:", path)
        shutil.rmtree(path)
        deleted.append(name)

    return sorted(deleted)


# Test code
for old in ["workspace", "backups"]:
    if os.path.exists(old):
        shutil.rmtree(old)

os.mkdir("workspace")

for name in [
    "a.log",
    "b.log",
    "incidents.csv",
    "summary.json",
    "incidents.pkl",
    "notes.txt"
]:
    with open(os.path.join("workspace", name), "w") as f:
        f.write(f"Test file: {name}\n")

print(organize("workspace"))
print(sorted(os.listdir("workspace")))

for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
    path = create_backup("workspace", "backups", label)
    print(os.path.basename(path), verify_backup("workspace", path))
    
os.remove(
    os.path.join(
        "backups",
        "backup_2026-10-03",
        "logs",
        "a.log"
    )
)

print(
    verify_backup(
        "workspace",
        os.path.join("backups", "backup_2026-10-03")
    )
)

print(cleanup_old_backups("backups", 2))
print(sorted(os.listdir("backups")))
