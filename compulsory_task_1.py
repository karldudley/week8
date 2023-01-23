class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office(self):
        print("The head office is in Cape Town")

class OOPCourse(Course):
    description = "OOP Fundamentals"
    trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"This course is all about {self.description} and the trainer is {self.trainer}.")

    def show_course_id(self):
        print("The course ID is #12345")

# create object and call methods
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
