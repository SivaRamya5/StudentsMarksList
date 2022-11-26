# python program for accepting 10 students 10 subjects marks find out the total marks ,avg marks of each students
# find out the total marks ,avg marks  highest and lowest marks.
class Student:
    marks = []

    def getData(self, rollno, name, m1, m2, m3, m4, m5):
        Student.rollno = rollno
        Student.name = name
        Student.marks.append(m1)
        Student.marks.append(m2)
        Student.marks.append(m3)
        Student.marks.append(m4)
        Student.marks.append(m5)

    def displayData(self):
        print("Roll Number is: ", Student.rollno)
        print("Name is: ", Student.name)
        # print ("Marks in subject 1: ", Student.marks[0])
        # print ("Marks in subject 2: ", Student.marks[1])
        # print ("Marks in subject 3: ", Student.marks[2])
        # print ("Marks in subject 4: ", Student.marks[3])
        # print ("Marks in subject 5: ", Student.marks[4])
        print("Marks are : ", Student.marks)
        print("Marks are: " , self.total())
        print("Total Marks are: ", self.total())
        print("Average Marks are: ", self.average())
        print("Highest marks", max(m1, m2, m3, m4, m5))
        print("Lowest marks", min(m1, m2, m3, m4, m5))




    def total(self):
        return (Student.marks[0] + Student.marks[1] + Student.marks[2] + Student.marks[3] + Student.marks[4])


    def average(self):
        return ((Student.marks[0] + Student.marks[1] + Student.marks[2]+ Student.marks[3] + Student.marks[4]) / 5)

for i in range(1,11):

   rollno = int(input("Enter the roll number of student"+str(i)+":"))
   name = input("Enter the name : ")
   m1 =float(input("Enter the marks in the  marketing : "))
   m2 = float(input("Enter the marks in the python : "))
   m3 = float(input("Enter the marks in the sql  : "))
   m4 = float(input("Enter the marks in the HRA : "))
   m5 = float(input("Enter the marks in the statistics  : "))



Student = Student()
Student.getData(rollno, name, m1, m2, m3, m4, m5)
Student.displayData()

