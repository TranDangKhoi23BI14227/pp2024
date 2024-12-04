def NumberOfStudent():
    return int(input("Number of students: "))

def InputStudentInfo(studentList: list, studentNumber: int):
    for i in range(studentNumber):
        studentInfo = {
            "ID": input("Input student ID: "),
            "Name": input("Input student name: "),
            "DoB": input("Input student DoB: ")
        }
        studentList.append(studentInfo)
        
def NumberOfCourse():
    return int(input("Number of courses: "))

def InputCourseInfo(courseList: list, courseNumber: int):
    for i in range(courseNumber):
        courseInfo = {
            "ID": input("Input course ID: "),
            "Name": input("Input course name: "),
            "Mark": {}
        }
        courseList.append(courseInfo)
        
def input_mark(student_list, course_list):
    
    
    chosen_course = []

    course_id = input("Enter the course ID you'd like to input mark: ")
    
    for temp in course_list:
        print(course_id)
        if course_id == temp[0]:
            chosen_course = temp
            
    if not chosen_course:
        print("No info found")
        return
    
    for student in student_list:
        mark_input ={"Student" : str(chosen_course[0]) , "Mark" : float(input("Enter the student mark: "))}
        chosen_course.append(mark_input)

    for student in student_list:
        print("Course"+ str(chosen_course[0]) + str(student[0]) + str(chosen_course[2]))

studentList = []
courseList = []
studentNumber=0
courseNumber=0
while True:
    print("List of possible actions:\n \
        1. Input number of students in a class\n \
        2. Input student information\n \
        3. Input number of courses\n \
        4. Input course information\n \
        5. Select a course, input marks for student\n \
        6. Print course list\n \
        7. Print student list\n \
        8. Print student marks\n \
        9. Exit")
    action = int(input("Choose your action: "))
    
    if action == 1:
        studentNumber = NumberOfStudent()
    elif action == 2:
        InputStudentInfo(studentList, studentNumber)
    elif action == 3:
        courseNumber = NumberOfCourse()
    elif action == 4:
        InputCourseInfo(courseList, courseNumber)
    elif action == 5:
        InputStudentMark(courseList, studentList)
    elif action == 6:
        PrintListCourse(courseList)
    elif action == 7:
        PrintStudentList(studentList)
    elif action == 8:
        PrintStudentMark(courseList)
    elif action == 9:
        break
    else:
        print("Invalid choice")