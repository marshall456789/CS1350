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
     result.append(student)        return sorted(result)


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