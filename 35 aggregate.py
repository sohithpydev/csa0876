def calculate_grade(marks):
    total_marks = sum(marks)
    aggregate = total_marks / len(marks)

    if aggregate > 75:
        grade = "Distinction"
    elif 60 <= aggregate < 75:
        grade = "First Division"
    elif 50 <= aggregate < 60:
        grade = "Second Division"
    elif 40 <= aggregate < 50:
        grade = "Third Division"
    else:
        grade = "Fail"

    return total_marks, aggregate, grade

def main():
    try:
        marks = [float(input(f"Enter marks for subject {i + 1}: ")) for i in range(4)]
        total_marks, aggregate, grade = calculate_grade(marks)

        print(f"\nTotal Marks: {total_marks}")
        print(f"Aggregate: {aggregate:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input. Please enter valid numerical marks.")

if __name__ == "__main__":
    main()
