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

class Coach(Person):
    def __init__(self, name, age, gender, expertise):
        super().__init__(name, age, gender)
        self.expertise = expertise

class Internship:
    def __init__(self, title, topics, start_date, duration_months):
        self.title = title
        self.topics = topics
        self.start_date = start_date
        self.duration_months = duration_months

class Application:
    applications = []

    @classmethod
    def submit_application(cls, student, internship):
        application = {
            'student': student,
            'internship': internship
        }
        cls.applications.append(application)

# Creating instances of the classes
student1 = Student("Alice", 20, "Female", "S12345", "Computer Science", 3, 3.8, ["Python", "Java"])
company1 = Company("TechCorp", "Silicon Valley", "Technology", 1000, "www.techcorp.com", "contact@techcorp.com")
center1 = InternshipCenter("CenterX", "Cityville", "John Doe", 50)
coach1 = Coach("Coach Bob", 30, "Male", "Software Development")
center1.coaches.append(coach1)
internship1 = Internship("Software Engineering Intern", ["Web Development", "Machine Learning"], "2023-09-01", 6)

# Students apply for an internship
Application.submit_application(student1, internship1)

# Querying applications
for application in Application.applications:
    student = application['student']
    internship = application['internship']
    print(f"{student.name} applied for {internship.title} internship.")

# Simulate student selecting an internship topic
student1.selected_topic = "Machine Learning"

# Restarting the application process
Application.applications = []

