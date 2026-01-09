# student.py
# Student Grade Calculator (CI / Jenkins Safe)

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3


def assign_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def main():
    import sys

    print("=== Student Grade Calculator ===")

    # Command-line execution (Jenkins safe)
    if len(sys.argv) == 7:
        name = sys.argv[1]
        department = sys.argv[2]
        semester = int(sys.argv[3])
        m1 = float(sys.argv[4])
        m2 = float(sys.argv[5])
        m3 = float(sys.argv[6])

        print("\n=== Program Parameters ===")
        print(f"Student Name : {name}")
        print(f"Department   : {department}")
        print(f"Semester     : {semester}")
        print(f"Marks        : {m1}, {m2}, {m3}")

        avg = calculate_average(m1, m2, m3)
        grade = assign_grade(avg)

        print(f"\nAverage = {avg:.2f}")
        print(f"Grade   = {grade}")

    else:
        print("Interactive mode disabled in CI environment.")
        print("Usage:")
        print("python student.py <name> <dept> <semester> <m1> <m2> <m3>")


if __name__ == "__main__":
    main()
