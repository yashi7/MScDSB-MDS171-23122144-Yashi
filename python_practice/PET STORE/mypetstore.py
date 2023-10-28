class petstore:
    def __init__(self):
        self.pets={
            "dogs":[],
            "cats":[]

        }
        
        
    def add_details(self,type,breed,age,gender,price):
            details={
                "breed":breed,
                "age":age,
                "gender":gender,
                "price":price,
            }
            if type=="dogs":
                self.pets["dogs"].append(details)
            elif type=="cats":
                self.pets["cats"].append(details)
    def search(self):
        type=input("enter the type of pet")
        breed=input("enter the breed")
        if type in self.pets:
            for item in self.pets[type]:
                if item["breed"]==breed:
                    print(item)
    def sell(self):
      type=input("enter the type")
      breed=input("enter the breed")
      if type in self.pets:
        for item in self.pets[type]:
          if item["breed"]==breed:
            print("your order is done \n","please pay:",item["price"])

            
    def print(self):
        print(self.pets)

def collectInput():
    breed = input("Enter the breed ")
    age = input("Enter age ")
    gender = input("Enter gender")
    price = input("enter the price ")
    return breed, age, gender, price

pets=petstore()

while True:
    print("1. add a dog")
    print("2. add a cat")
    print("3. search the pet")
    print("4. sell a pet")
    print("5. print the pets")
    print("6. exit")

    choice=input("enter ypur choice")
    if choice=="1":
        breed,age,gender,price= collectInput()
        pets.add_details("dogs",breed,age,gender,price)
    elif choice=="2":
        breed,age,gender,price=collectInput()
        pets.add_details("cats",breed,age,gender,price)
    elif choice=="3":
        pets.search()
    elif choice=="4":
        pets.sell()
    elif choice=="5":
        pets.print()
    elif choice=="6":
        exit()
    else:
        print("yes")
