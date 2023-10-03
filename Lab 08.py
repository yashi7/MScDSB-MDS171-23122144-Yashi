#Write a Python program to implement a Stack class that has the following functions
# Push Item
# Pop Item
# Print the Items in the stack
# Size of Stack
# The top item in the stack
# Check if the stack is empty
# search the item


class Stack:
    def __init__(self):
        self.stack =[]
    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def remove(self):
        if len(self.stack)<=0:
            return ("no element in stack")
        else:
            return self.stack.pop()
    def show(self):
        print("the items are :")
        for i in self.stack:
            print(i)
    def size(self):
        print("The size of the stack is :",len(self.stack))
    def retrieve(self):
        print("the top item is:",self.stack[len(self.stack)-1])
    def check_empty(self):
        if len(self.stack)==0:
            print("The stack is empty")
        else:
            print("Stack is not empty")
    def search(self,a):
            if a in self.stack:
                print("present in stack")
            else:
                print("not in stack")

checking_stack=Stack()
while True:
    print("1. Add item")
    print("2. Pop item")
    print("3. Print all the items")
    print("4. Print the size of the Stack")
    print("5. Print the top item")
    print("6. Check if the stack is empty")
    print("7. Search the item")
    print("8. Exit")

    choice=int(input("enter your choice:").strip())

    if choice == 1:
        print("add an item to the list")
        data = input("Enter the value")
        checking_stack.push(data)
    elif choice == 2:   
        checking_stack.remove()
    elif choice == 3:
        checking_stack.show()
    elif choice == 4:
        checking_stack.size()
    elif choice==5:
        checking_stack.retrieve()
    elif choice==6:
        checking_stack.check_empty()
    elif choice==7:
        a=input("enter the data you want to search")
        checking_stack.search(a)
    elif choice==8:
        exit()
        

