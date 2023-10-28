#create a menu driven program that collects student details
        #name
        #email
        #phone
        #use dictionary to store the student details
        #menu option
        #1. create students
        #search for students
        #print students
def details(name,register_no,email,phone):
    name=input("enter a name")
    register_no=input("enter register no")
    email=input("enter the email")
    phone=input("enter phone number")
    return name,register_no,email,phone

student_dict={}
def createstudent(name,register_no,email,phone):
    student={
    
        "name":name,
        "email":email,
        "phone":phone
    }
    student_dict[register_no]=student

print("register_no\tname\temail\tphone")
for register_no in student_dict.keys():
    print(register_no,end="\t")
    for key in student_dict[register_no]:
        print(student_dict[register_no][key],end='\t')
    print()
    
while True:
    print("Menu Options")
    print("1. Enter Student Info")
    print("2. List Students")
    print("3. Exit")

    choice = input("Enter the choice").strip()
    if choice == "1":
        name, register_no, email, phone = details()
        createstudent(name, register_no, email, phone)
    elif choice == "2":
        print()
    elif choice == "3":
        exit()
    else:
        print("Invalid Choice")
        