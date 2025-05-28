university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#Q1: Print all student names and their majors
print("Student Names and Majors:")
for student_id, details in university_data.items():
    print(f"{details['name']} - {details['major']}")

#Q2: Average score per course per student
print("Average score per course per student:")
for student_id, details in university_data.items():
    print(f"{details['name']}:")
    for course, scores in details['courses'].items():
        avg = sum(scores.values()) / len(scores)
        print(f"  {course}: {avg:.2f}")

#Q3: Find students who scored >90 in final of Python101
print("Students scoring >90 in Python101 Final")
for student_id, details in university_data.items():
    course_data = details['courses'].get("Python101")
    if course_data and course_data.get("final", 0) > 90:
        print(f"{details['name']} scored {course_data['final']} in Python101 final")

#Q4: Add new course AI101 for student S101
print(": Adding new course AI101 to S101")
university_data["S101"]["courses"]["AI101"] = {"midterm": 85, "final": 90, "project": 88}
print(f"Updated courses for {university_data['S101']['name']}:")
print(university_data["S101"]["courses"])

#Q5: Print average for each course (across all students)
from collections import defaultdict

print("Average for each course (all students combined)")

course_totals = defaultdict(list)

# Accumulate all scores
for details in university_data.values():
    for course, scores in details["courses"].items():
        avg_score = sum(scores.values()) / len(scores)
        course_totals[course].append(avg_score)

# Compute average per course
for course, averages in course_totals.items():
    overall_avg = sum(averages) / len(averages)
    print(f"{course}: {overall_avg:.2f}")
