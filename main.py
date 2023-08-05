class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, student_id, major, year, gpa, skills):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major
        self.year = year
        self.gpa = gpa
        self.skills = skills
        self.selected_topic = None
        self.internship = None

    def apply_for_internship(self, internship):
        Application.submit_application(self, internship)

    def delete_internship(self):
        if self.internship:
            self.internship.remove_student(self)
            self.internship = None

class Company:
    def __init__(self, name, location, industry, size, website, contact_email):
        self.name = name
        self.location = location
        self.industry = industry
        self.size = size
        self.website = website
        self.contact_email = contact_email

class InternshipCenter:
    def __init__(self, name, location, coordinator, capacity):
        self.name = name
        self.location = location
        self.coordinator = coordinator
        self.capacity = capacity
        self.coaches = []
        self.internships = []

    def add_coach(self, coach):
        self.coaches.append(coach)

    def create_internship(self, title, topics, start_date, duration_months):
        internship = Internship(title, topics, start_date, duration_months, self)
        self.internships.append(internship)
        return internship

class Coach(Person):
    def __init__(self, name, age, gender, expertise):
        super().__init__(name, age, gender)
        self.expertise = expertise

class Internship:
    def __init__(self, title, topics, start_date, duration_months, center):
        self.title = title
        self.topics = topics
        self.start_date = start_date
        self.duration_months = duration_months
        self.center = center
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.internship = self

    def remove_student(self, student):
        self.students.remove(student)
        student.internship = None

class Application:
    applications = []

    @classmethod
    def submit_application(cls, student, internship):
        application = {
            'student': student,
            'internship': internship
        }
        cls.applications.append(application)

    @classmethod
    def get_applications(cls):
        return cls.applications

# Interactive input
def input_student():
    name = input("Student Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    student_id = input("Student ID: ")
    major = input("Major: ")
    year = int(input("Year: "))
    gpa = float(input("GPA: "))
    skills = input("Skills (comma-separated): ").split(',')
    return Student(name, age, gender, student_id, major, year, gpa, skills)

def input_coach():
    name = input("Coach Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    expertise = input("Expertise: ")
    return Coach(name, age, gender, expertise)

def input_internship_center():
    name = input("Center Name: ")
    location = input("Location: ")
    coordinator = input("Coordinator: ")
    capacity = int(input("Capacity: "))
    return InternshipCenter(name, location, coordinator, capacity)

def input_internship():
    title = input("Internship Title: ")
    topics = input("Topics (comma-separated): ").split(',')
    start_date = input("Start Date: ")
    duration_months = int(input("Duration (months): "))
    return title, topics, start_date, duration_months


class InternshipManagementSystem:
    pass


ims = InternshipManagementSystem()

while True:
    print("\n1. Add Student")
    print("2. Add Coach")
    print("3. Add Internship Center")
    print("4. Add Internship")
    print("5. Apply for Internship")
    print("6. Delete Internship")
    print("7. Show Applications")
    print("8. Exit")

    choice = int(input("Select an option: "))

    if choice == 1:
        student = input_student()
        ims.add_student(student)
    elif choice == 2:
        coach = input_coach()
        ims.add_coach(coach)
    elif choice == 3:
        center = input_internship_center()
        ims.add_internship_center(center)
    elif choice == 4:
        title, topics, start_date, duration_months = input_internship()
        center = ims.internship_centers[0]  # Assuming only one center for simplicity
        internship = center.create_internship(title, topics, start_date, duration_months)
        ims.add_internship(internship)
    elif choice == 5:
        student_id = input("Enter Student ID: ")
        student = next((s for s in ims.students if s.student_id == student_id), None)
        if student:
            internship_id = int(input("Enter Internship ID: "))
            internship = next((i for i in ims.internships if i.center == center and i.duration_months == internship_id), None)
            if internship:
                student.apply_for_internship(internship)
                print("Application submitted.")
            else:
                print("Internship not found.")
        else:
            print("Student not found.")
    elif choice == 6:
        student_id = input("Enter Student ID: ")
        student = next((s for s in ims.students if s.student_id == student_id), None)
        if student:
            student.delete_internship()
            print("Internship deleted.")
        else:
            print("Student not found.")
    elif choice == 7:
        print("\nApplications:")
        for application in Application.get_applications():
            student = application['student']
            internship = application['internship']
            print(f"{student.name} applied for {internship.title} internship.")
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please select again.")


