#class MSCDSB:  #in the class we have data functions or members
   
    #def __init__(self): #initialization method used to initialize the variables of the class(it's a method of the class)
        #these are our data members or properties or attributes
        #self.name = "MSC DS B"
        #self.students = ["A","B","C"]

    #def printStudents(self):#member function
        #for student in self.students:
           # print(student)


#obj = MSCDSB()#object
#print(obj.name,obj.students)
#obj.printStudents()
#when we create a new object the init method will be called by default


# class car:

#     def __init__(self,mgf,mdl,yer):
#         self.manufacturer=mgf
#         self.model=mdl
#         self.year=yer
#     def __str__(self):
#         return self.manufacturer
# bmw=car("BMW","F series",2020)
# #print(bmw.manufacturer)       
# #ferari=car("ferari","A series",2023)
# #print(ferari.model)
# #print(bmw.year)
# #print(ferari.manufacturer)
   
# print(bmw)

# create a class restaurant that accepts
# item name  and quantity as input
# inside your class you are having the item
# and its price(unit price) as a dictionary
# create a function to claculate tottal Cost
# that prints the item name qty and total cost 

# class restaurant:
#     def __init__(self,itemname,qty):
#         self.itemname=itemname
#         self.quantity=qty
#         self.menuitem={
#             "rice":30,
#             "chapati":20,
#             "dal":40,
#             "chicken":70
#             }
#     def totalcost(self):
#         print("total cost of the order")
#         print("items\t",self.itemname)
#         print("quantity\t",self.quantity)
#         total=self.quantity * self.menuitem[self.itemname]
#         print("total\t",total)

# item=input("enter the item")
# quan=int(input("enter the quantity"))
# order=restaurant(item,quan)
# print(order.itemname,order.quantity)
# order.totalcost()
    
# define a class expense tracker that stores the 
# expenses and income in a dictionary
# implement the method to 
# - store the transaction
# - view transaction
# - calculate the total expense/income

class expenseTracker:
    def __init__(self):
        self.expensedict={
            "income":[],
            "expense":[],
        }
    def store_transactions(self,type,amt,category,date,details):
        trans={
            "amount":amt,
            "category":category,
            "date":date,
            "details":details,
        }
        if type == "income":
            self.expensedict["income"].append(trans)
        else:
            self.expensedict["expense"].append(trans)
    def view_transactions(self):
        print("your income:")
        for item in self.expensedict["income"]:
            print(item)
        print("your expense:")
        for item in self.expensedict["expense"]:
            print(item)
    def calculate_transactions(self):
        total_income=0
        for item in self.expensedict["income"]:
            total_income += item["ampount"]
        print("total income\t",total_income)
        total_expense=0
        for item in self.expensedict["expense"]:
            total_expense += item["amount"]
        print("total expense\t",total_expense)

#define a menu that will let users to enter expenses,view expenses
#or income, get totals in each and exit from the program
def collectInput():
    amt = int(input("Enter the amout: "))
    category = input("Enter Category: ")
    date = input("Enter Date (DD/MM/YYYY): ")
    details = input("Enter description: ")
    return amt, category, date, details

myexpense = expenseTracker()
while True:
    print("..MY EXPENSE TRACKER..")
    print("1. record income")
    print("2. record expense")
    print("3. view record")
    print("4. view my spending")
    print("5. exit")

    choice= int(input("enter your choice").strip())
    if choice==1:
        print("enter the details of income")
        amt,category,date,details = collectInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice==2:
        print("Enter the details of expense")
        amt, category, date, details = collectInput()
        myexpense.store_transactions("expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")
