def calculate_users(total_users, staff_users):
    student_users = total_users - staff_users
    non_teaching_staff = staff_users // 3

    return student_users, staff_users, non_teaching_staff

def main():
    total_users = int(input("Enter the total number of users in the college: "))
    staff_users = int(input("Enter the total number of staff users: "))

    student_users, staff_users, non_teaching_staff = calculate_users(total_users, staff_users)

    print(f"Number of student users: {student_users}")
    print(f"Number of staff users: {staff_users}")
    print(f"Number of non-teaching staff users: {non_teaching_staff}")

if __name__ == "__main__":
    main()
