
class Student:
    def __init__(self, name, major, dob, zipcode, emplid):
        self.name = name
        self.dob = dob
        self.major = major
        self.zipcode = zipcode
        self.emplid = emplid

    def __str__(self):
        list = ["tom", "12/5/22", "CS", 10567, 23456789]


class Management:
    def __init__(self):
        self.student_list = []

    def menu(self):
        print("--------------------------------------")
        print(" Welcome to student Management system")
        print("---------------------------------------")
        print("Press 1 to add a new student")
        print("Press 2 to search a student")
        print("Press 3 to delete a student")
        print("Press 4 to update a student information")
        print("Press 0 to exit the program")
        user = int(input())
        if user == 1:
            self.accept()
        elif user == 2:
            self.search()
        elif user == 3:
            self.delete()
        elif user == 4:
            self.update()
        elif user == 0:
            exit(0)

    def accept(self):
        name = (input("Input Name: "))
        dob = (input("Input MM/DD/YY: "))
        major = input("Input Major: ")
        zipcode = int(input("Input ZIP CODE: "))
        emplid = int(input("Input EMPLID ID: "))
        info = Student(name, major, dob, zipcode, emplid)
        self.student_list.append(info)

    def display(self):
        print("Name : ", self.student_list.name)
        print("DOB : ", self.student_list.dob)
        print("Major : ", self.student_list.major)
        print("ZIP code : ", self.student_list.zipcode)
        print("EMPLID ID : ", self.student_list.emplid)

    def search(self):
        emplid = int(input("Input EMPLID ID: "))
        for i in range(len(self.student_list)):
            if self.student_list[i].emplid == emplid:
                print(info)
            else:
                print("NOT FOUND!")

    def delete(self):
        emplid2 = int(input("Input EMPLID ID: "))
        i = self.student_list.search(emplid2)
        del (student_list[i])

    def update(self):
        emplid3 = int(input("Input EMPLID ID:"))
        i = student_list.search(emplid3)
        if i == found:
            print ("What would you like to change?")
            print("Enter 1 for ZIP CODE")
            print("Enter 2 for Major")
            person = int(input())
            if person == "1":
               new1=int(input("Enter new zip code:"))
               delattr(info, zipcode)
               info.append(new1)
            elif person == "2":
                new2=input("Enter new Major:")
                delattr(info, major)
                info.append(new2)
        else:
            print('Not found!')




obj = Student
obj2 = Management()
obj2.menu()
