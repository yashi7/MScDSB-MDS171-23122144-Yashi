name=""
product=""
quantity=""
def order(name,product,quantity):
    name=input("enter your name")
    product=input("enter the product")
    quantity=input("enter the quantity")
    return name,product,quantity

order_dict={}
def dict(name,product,quantity):
    details={
        "product":product,
        "quantity":quantity
    }
    order_dict[name]=details

def pri():
    for name in order_dict.keys():
        print(name,end="\t")
        for key in order_dict[name]:
            print(order_dict[name][key],end="\t")

while True:
    print("menu options")
    print("1. order details")
    print("2. list order")
    print("3.exit")

    choice=input("enter your choice")
    if choice=="1":
        name,product,quantity=order(name,product,quantity)
        dict(name,product,quantity)
    elif choice=="2":
        pri()
    elif choice=="3":
        exit()
    else:
        print("invalid")
    