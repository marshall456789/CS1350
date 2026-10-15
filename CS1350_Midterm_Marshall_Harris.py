
class Gradebook:
    def __init__(self):
        self.grades = {}

    def add_score(self, student, assignment, score):
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][assignment] = score

    def student_average(self, student):
        if student not in self.grades or not self.grades[student]:
            return None
        scores = self.grades[student].values()
        return sum(scores) / len(self.grades[student])

    def assignment_average(self, assignment):
        scores = []
        for student in self.grades:
            if assignment in self.grades[student]:
                scores.append(self.grades[student][assignment])
        if not scores:
            return None
        return sum(scores) / len(scores)

    def top_students(self, n):
        averages = []
        for student in self.grades:
            average = self.student_average(student)
            if average is not None:
                averages.append((student, average))
        averages.sort(key=lambda item: (-item[1], item[0]))
        return [student for student, average in averages[:n]]

    def missing(self, assignment):
        result = []
        for student in self.grades:
            if assignment not in self.grades[student]:
                result.append(student)
        return sorted(result)


# Test cases
gb = Gradebook()

gb.add_score("Alice", "hw1", 90)
gb.add_score("Alice", "hw2", 80)
gb.add_score("Bob", "hw1", 70)
gb.add_score("Bob", "hw2", 60)
gb.add_score("Carol", "hw1", 100)
gb.add_score("Bob", "hw2", 75)


print(gb.student_average("Alice"))
print(gb.student_average("Bob"))
print(gb.student_average("Zed"))
print(gb.assignment_average("hw1"))
print(gb.assignment_average("hw9"))
print(gb.top_students(2))
print(gb.missing("hw2"))





from abc import ABC, abstractmethod


class Shipment(ABC):
    def __init__(self, tracking_id, weight_kg):
        self.validate_weight(weight_kg)
        self.tracking_id = tracking_id
        self.weight_kg = weight_kg

    @abstractmethod
    def cost(self):
        pass

    def label(self):
        return (
            f"{self.tracking_id} ({self.weight_kg} kg): "
            f"${self.cost():.2f}"
        )

    @staticmethod
    def validate_weight(weight_kg):
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")


class StandardShipment(Shipment):
    def __init__(self, tracking_id, weight_kg, rate_per_kg=2.00):
        super().__init__(tracking_id, weight_kg)
        self.rate_per_kg = rate_per_kg

    def cost(self):
        return self.weight_kg * self.rate_per_kg


class ExpressShipment(StandardShipment):
    def __init__(
        self, tracking_id, weight_kg,
        rate_per_kg=2.00, surcharge=10.00
    ):
        super().__init__(tracking_id, weight_kg, rate_per_kg)
        self.surcharge = surcharge

    def cost(self):
        return super().cost() + self.surcharge


class InternationalShipment(Shipment):
    def __init__(
        self, tracking_id, weight_kg, country, customs_pct=0.15
    ):
        super().__init__(tracking_id, weight_kg)
        self.country = country
        self.customs_pct = customs_pct

    def cost(self):
        return self.weight_kg * 5.00 * (1 + self.customs_pct)


def manifest(shipments):
    total = 0

    for shipment in shipments:
        print(shipment.label())
        total += shipment.cost()

    print(f"Total: ${total:.2f}")
    return total




# Test cases
shipments = [
    StandardShipment("S100", 4.0),
    ExpressShipment("E200", 2.5),
    InternationalShipment("I300", 3.0, country="Canada"),
]

total = manifest(shipments)

try:
    Shipment.validate_weight(-1)
except ValueError as e:
    print("Caught:", e)
    
    
    
    
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
