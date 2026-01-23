import copy

# --- DATABASE INITIALIZATION ---
students = []        # List to store all students
student_ids = set()  # Track unique student IDs
emails = set()       # Track unique emails

# --- FUNCTIONS ---

# 1️⃣ Add Student
def add_student():
    try:
        sid = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID! Must be a number.")
        return
    
    if sid in student_ids:
        print(">> Error: Student ID already exists!")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")

    if email in emails:
        print(">> Error: Email already exists!")
        return

    # Input subjects
    subjects = {}
    for subject in ["Math", "English", "Science"]:
        try:
            mark = int(input(f"Enter marks for {subject}: "))
        except ValueError:
            mark = 0
        subjects[subject.lower()] = mark

    # Input skills as comma-separated string → convert to set
    skills_input = input("Enter skills (comma-separated): ")
    skills = set(map(str.strip, skills_input.split(",")))

    # Create student dictionary
    student = {
        "id": sid,
        "name": name,
        "email": email,
        "subjects": subjects,
        "skills": skills
    }

    students.append(student)
    student_ids.add(sid)
    emails.add(email)
    print(f">> Student {name} added successfully!\n")


# 2️⃣ Update Student
def update_student():
    try:
        sid = int(input("Enter ID of student to update: "))
    except ValueError:
        print("Invalid ID!")
        return

    for stu in students:
        if stu.get("id") == sid:
            print(f"Updating Student: {stu.get('name')}")
            
            # Shallow Copy Demo
            shallow_copy = stu.copy()
            print("Shallow Copy created. Modifying nested dict will affect original!")

            # Deep Copy Demo
            deep_copy = copy.deepcopy(stu)
            print("Deep Copy created. Modifying nested dict will NOT affect original!\n")

            # Update Options
            print("1. Update Name\n2. Update Email\n3. Update Subject Marks\n4. Add Skill")
            choice = input("Choose what to update: ")

            if choice == "1":
                new_name = input("Enter new name: ")
                stu["name"] = new_name
            elif choice == "2":
                new_email = input("Enter new email: ")
                if new_email in emails:
                    print(">> Email already exists!")
                    return
                emails.discard(stu["email"])  # remove old email
                stu["email"] = new_email
                emails.add(new_email)
            elif choice == "3":
                subject = input("Enter subject to update (math/english/science): ").lower()
                if subject in stu["subjects"]:
                    try:
                        marks = int(input("Enter new marks: "))
                    except ValueError:
                        marks = stu["subjects"][subject]
                    stu["subjects"][subject] = marks
                else:
                    print(">> Invalid subject!")
            elif choice == "4":
                skill = input("Enter skill to add: ").strip()
                stu["skills"].add(skill)
            else:
                print("Invalid choice!")

            print(">> Update complete!\n")
            return

    print(">> Student not found!\n")


# 3️⃣ Print Student Info
def print_student_info():
    try:
        sid = int(input("Enter student ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    for stu in students:
        if stu.get("id") == sid:
            print("\n--- Profile ---")
            print(f"ID: {stu.get('id')}")
            print(f"Name: {stu.get('name')}")
            print(f"Email: {stu.get('email')}")
            print(f"Subjects: {stu.get('subjects')}")
            print(f"Skills: {stu.get('skills')}\n")
            return

    print(">> Student not found!\n")


# 4️⃣ Analytics
def analytics():
    if not students:
        print(">> No students yet!\n")
        return

    print("Analytics Options:")
    print("1. Average Marks for a Student")
    print("2. Topper in a Subject")
    print("3. All Unique Skills")
    print("4. Count Students with a Skill")
    
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            sid = int(input("Enter student ID: "))
        except ValueError:
            print("Invalid ID!")
            return
        for stu in students:
            if stu.get("id") == sid:
                subjects = stu.get("subjects", {})
                if subjects:
                    avg = sum(subjects.values()) / len(subjects)
                    print(f"Average Marks for {stu.get('name')}: {avg}\n")
                else:
                    print("No subjects found.\n")
                return
        print("Student not found.\n")

    elif choice == "2":
        subject = input("Enter subject (math/english/science): ").lower()
        topper = None
        max_marks = -1
        for stu in students:
            marks = stu.get("subjects", {}).get(subject)
            if marks is not None and marks > max_marks:
                max_marks = marks
                topper = stu
        if topper:
            print(f"Topper in {subject.capitalize()}: {topper.get('name')} with {max_marks} marks\n")
        else:
            print("No data found for this subject.\n")

    elif choice == "3":
        all_skills = set()
        for stu in students:
            all_skills |= stu.get("skills", set())
        print(f"All Unique Skills: {all_skills}\n")

    elif choice == "4":
        skill = input("Enter skill to count: ").strip()
        count = 0
        for stu in students:
            if skill in stu.get("skills", set()):
                count += 1
        print(f"Number of students with skill '{skill}': {count}\n")
    else:
        print("Invalid choice!\n")


# --- MAIN LOOP ---
while True:
    print("\n" + "="*40)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Student")
    print("2. Update Student")
    print("3. Show Student Info")
    print("4. Analytics")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        print_student_info()
    elif choice == "4":
        analytics()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
