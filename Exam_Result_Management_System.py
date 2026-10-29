import json
import os

FILE = "results.txt"


def load_records():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_records():
    with open(FILE, "w") as f:
        json.dump(records, f, indent=4)


def total(maths, physics, chemistry):
    return maths + physics + chemistry


def percentage(total_marks):
    return total_marks / 3


def result(maths, physics, chemistry):
    if maths >= 40 and physics >= 40 and chemistry >= 40:
        return "Pass"
    return "Fail"


records = load_records()

while True:
    print("\n--- Exam Result Management System ---")
    print("1. Add Student")
    print("2. View All")
    print("3. Rank List")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")

        if any(s["roll"] == roll for s in records):
            print("Roll number", roll, "already exists.")
            continue

        name = input("Enter student name: ")

        try:
            maths = int(input("Enter Maths marks: "))
            physics = int(input("Enter Physics marks: "))
            chemistry = int(input("Enter Chemistry marks: "))
        except ValueError:
            print("Marks must be numbers.")
            continue

        if any(m < 0 or m > 100
               for m in [maths, physics, chemistry]):
            print("Marks must be between 0 and 100.")
            continue

        t = total(maths, physics, chemistry)
        p = percentage(t)
        r = result(maths, physics, chemistry)

        student = {
            "roll": roll,
            "name": name,
            "maths": maths,
            "physics": physics,
            "chemistry": chemistry,
            "total": t,
            "percentage": p,
            "result": r
        }

        records.append(student)
        save_records()

        print("Record added:", roll, "|", name)
        print("Total:", t, "| Percentage: {:.2f}%".format(p),
              "| Result:", r)

    elif choice == "2":
        for s in records:
            print(s)

    elif choice == "3":
        ranked = sorted(
            records, key=lambda s: s["total"], reverse=True
        )

        for i, s in enumerate(ranked, start=1):
            print(
                "Rank", i, "|", s["roll"], "|", s["name"],
                "|", s["total"],
                "| {:.2f}%".format(s["percentage"]),
                "|", s["result"]
            )

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")