class petstore:
    def __init__(self):
        self.pets={
            "dogs":[],
            "cats":[]
        }
        
        
    def add_details(self,type,breed,age,gender,price):
            self.pets[type].append({
                "breed":breed,
                "age":age,
                "gender":gender,
                "price":price,
            })
            # if type=="dogs":
            #     self.pets["dogs"].append(details)
            # elif type=="cats":
            #     self.pets["cats"].append(details)
    def search(self,type):
        type=input("enter the type of pet")
        if type in self.pets:
            for item in self.pets[type]:
                print(item)
        # for item in self.pets[type]:
        #     for i in self.pets.values(i):
        #         if i == type:
        #             print("true")
        #         else:
        #             print("false")
    # def sell(self,type):
    #     type=input("enter the type of pet you want ")
    #     for item in self.pets[type]:
    #         for i in self.pets.values(i):
    #             print(self.pets[item]['price'][i])
    #             self.pets["dogs"].pop(i)
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
        breed,age,gender,price=pets.collectInput()
        pets.add_details("cats",breed,age,gender,price)
    elif choice=="3":
        pets.search()
    elif choice=="4":
        pets.sell()
    elif choice=="5":
        pets.print()
    elif choice=="5":
        exit



