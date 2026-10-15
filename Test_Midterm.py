
import json

def process_readings(in_file, json_file, alert_file, limit):
    """
    Summarize sensor readings into a JSON file and write alerts.

    Returns:
        number of alert lines written
    """
    sensors = {}

    with open(in_file, "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue

            timestamp, sensor_id, value_text = line.split(",")
            value = float(value_text)

            if sensor_id not in sensors:
                sensors[sensor_id] = {
                    "count": 0,
                    "total": 0,
                    "max": value
                }

            sensors[sensor_id]["count"] += 1
            sensors[sensor_id]["total"] += value

            if value > sensors[sensor_id]["max"]:
                sensors[sensor_id]["max"] = value

    
    summary = {}

    for sensor_id, data in sensors.items():
        summary[sensor_id] = {
            "count": data["count"],
            "average": data["total"] / data["count"],
            "max": data["max"]
        }

    with open(json_file, "w") as f:
        json.dump(summary, f, indent=2)

    alert_count = 0

    with open(in_file, "r") as f:
        with open(alert_file, "w") as alerts:
            for line in f:
                line = line.strip()

                if line == "":
                    continue

                timestamp, sensor_id, value_text = line.split(",")

                if float(value_text) > limit:
                    alerts.write(
                        f"{timestamp} {sensor_id} {value_text}\n"
                    )
                    alert_count += 1

    return alert_count


# Test cases
with open("readings.txt", "w") as f:
    f.write("08:00,temp1,21.5\n")
    f.write("08:00,temp2,19.0\n")
    f.write("\n")
    f.write("08:10,temp1,26.0\n")
    f.write("08:10,temp2,18.5\n")
    f.write("08:20,temp1,24.5\n")

alerts = process_readings(
    "readings.txt", "summary.json", "alerts.txt", 24.0
)

print(alerts)

with open("summary.json", "r") as f:
    summary = json.load(f)

print(summary["temp1"])
print(summary["temp2"])

with open("alerts.txt", "r") as f:
    print(f.read())
