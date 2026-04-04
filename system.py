class System:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")

        if student_id in self.students:
            print("Student already exists")
            return

        self.students[student_id] = name
        print("Student added successfully")

    def add_course(self):
        course_id = int(input("Enter Course ID: "))
        name = input("Enter Course Name: ")
        capacity = int(input("Enter Course Capacity: "))

        if course_id in self.courses:
            print("Course already exists")
            return

        self.courses[course_id] = {
            "name": name,
            "capacity": capacity,
            "students": set()
        }

        print("Course added successfully")

    def enroll(self):
        student_id = int(input("Enter Student ID: "))
        course_id = int(input("Enter Course ID: "))

        if student_id not in self.students:
            print("Student not found")
            return

        if course_id not in self.courses:
            print("Course not found")
            return

        course = self.courses[course_id]

        # UPDATE: Prevent duplicate enrollment
        if student_id in course["students"]:
            print("Student already enrolled")
            return

        # UPDATE: Capacity check
        if len(course["students"]) >= course["capacity"]:
            print("Course is full")
            return

        course["students"].add(student_id)
        print("Enrollment successful")

    def search_student(self):
        student_id = int(input("Enter Student ID to search: "))

        # UPDATE: O(1) lookup using dictionary
        if student_id in self.students:
            print("Student Found:", self.students[student_id])
        else:
            print("Student not found")

    def show_students_in_course(self):
        course_id = int(input("Enter Course ID: "))

        if course_id not in self.courses:
            print("Course not found")
            return

        student_ids = list(self.courses[course_id]["students"])

        # UPDATE: Sorting by name (O(n log n))
        sorted_students = sorted(student_ids, key=lambda x: self.students[x])

        print("Students in course:")
        for sid in sorted_students:
            print(sid, "-", self.students[sid])


# MAIN PROGRAM
system = System()

while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Search Student")
    print("5. Show Students in Course")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()
    elif choice == "2":
        system.add_course()
    elif choice == "3":
        system.enroll()
    elif choice == "4":
        system.search_student()
    elif choice == "5":
        system.show_students_in_course()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")