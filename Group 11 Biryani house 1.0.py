VegBir = {"item": "Veg Biryani", "MRP": 250}
ChickBir = {"item": "Chicken Biryani", "MRP": 350}
ShaBir = {"item": "Shahi Biryani", "MRP": 350}
HydraBir = {"item": "Hyderabadi Biryani", "MRP": 400}
MughBir = {"item": "Mughlai Biryani", "MRP": 450}
MuttBir = {"item": "Mutton Biryani", "MRP": 500}
BeefBir = {"item": "Beef Biryani", "MRP": 600}

BiryaniList = ["Veg Biryani", "Chicken Biryani", "Shahi Biryani", "Hyderabadi Biryani", "Mughlai Biryani", "Mutton Biryani", "Beef Biryani"]

VegShaw = {"item": "Veg Shawarma", "MRP": 100}
ChickShaw = {"item": "Chicken Shawarma", "MRP": 150}
MuttShaw = {"item": "Mutton Shawarma", "MRP": 175}
BBQShaw = {"item": "BBQ Shawarma", "MRP": 175}
LebShaw = {"item": "Lebanese Shawarma", "MRP": 200}
BeefShaw = {"item": "Beef Shawarma", "MRP": 200}

ShawarmaList = ["Veg Shawarma" , "Chicken Shawarma" , "Mutton Shawama" , "BBQ Shawarma" , "Lebanese Shawarma" , "Beef Shawarma"]

Tea = {"item": "Tea", "MRP": 20}
Coffee = {"item": "Coffee", "MRP": 30}
Lemon = {"item": "Lemonade", "MRP": 30}
Soda = {"item": "Soft Drinks", "MRP": 40}
MlkShk = {"item": "Milkshake", "MRP": 50}

BeverageList = ["Tea" , "Coffee" , "Lemonade" , "Soft Drink" , "Milk Shake"]

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
print(f"{Fore.LIGHTCYAN_EX}{Back.BLACK}=== WELCOME TO GROUP 11 BIRYANI HOUSE ===")
print(f"\n{Fore.LIGHTCYAN_EX}---Welcome to the Billing Section---")
finalorder = {}
temporder = {}
cont = "y"
while cont == "y" or cont == "Y" or cont == "yes" or cont == "Yes":
    print(f"{Fore.MAGENTA}\t-Press 1 for Biryani\n\t-Press 2 for Shawarma\n\t-Press 3 for Beverage")
    billingchoice = input("Enter Choice here: ")
    if billingchoice == "1":
        print("You have chosen Biryani.")
        print(f"{Style.BRIGHT}\t-Press 1 for Veg Biryani\n\t-Press 2 for Chicken Biryani\n\t-Press 3 for Shahi Biryani\n\t-Press 4 for Hyderabadi Biryani\n\t-Press 5 for Mughlai Biryani\n\t-Press 6 for Mutton Biryani\n\t-Press 7 for Beef Biryani")
        order = input("Enter option here: ")
        if order == "1": # VEG BIRYANI
            print(f"-You have chosen {VegBir['item']}.")
            qty = int(input(f"\t-How many plates of {BiryaniList[0]} do you want?: "))
            temporder[BiryaniList[0]] = [VegBir['MRP'] , qty]
        elif order == "2": # CHICKEN BIRYANI
            print(f"You have chosen {ChickBir['item']}")
            qty = int(input(f"\t-How many plates of {BiryaniList[1]} do you want?: "))
            temporder[BiryaniList[1]] = [ChickBir['MRP'] , qty]
        elif order == "3": # SHAHI BIRYANI
            print(f"You have chosen {ShaBir['item']}")
            qty = int(input(f"\t-How many plates of {BiryaniList[2]} do you want?: "))
            temporder[BiryaniList[2]] = [ShaBir['MRP'] , qty]
        elif order == "4": # HYDRABADI BIRYANI
            print(f"You have chosen {HydraBir['item']}")
            qty = int(input(f"\t-How many plates of {BiryaniList[3]} do you want?: "))
            temporder[BiryaniList[3]] = [HydraBir['MRP'] , qty]
        elif order == "5": # MUGHLAI BIRYANI
            print(f"You have chosen {MughBir['item']}")
            qty = int(input(f"\t-How many plates of {BiryaniList[4]} do you want?: "))
            temporder[BiryaniList[4]] = [MughBir['MRP'] , qty]
        elif order == "6": # MUTTON BIRYANI
            print(f"You have chosen {MuttBir['item']}")
            qty = int(input(f"\t-How many plates of {BiryaniList[5]} do you want?: "))
            temporder[BiryaniList[5]] = [MuttBir['MRP'] , qty]
        elif order == "7": # BEEF BIRYANI
            print(f"You have chosen {BeefBir['item']}")
            qty = int(input(f"\t-How many plates of {BiryaniList[6]} do you want?: "))
            temporder[BiryaniList[6]] = [BeefBir['MRP'] , qty]
        else:
            print("Did not recieve correct input. Please try again.")
    if billingchoice == "2":
        print("You have chosen Shawarma.")
        print(f"{Style.BRIGHT}\tPress 1 for Veg Shawarma\n\tPress 2 for Chicken Shawarma\n\tPress 3 for Mutton Shawarma\n\tPress 4 for BBQ Shawarma\n\tPress 5 for Lebanese Shawarma\n\tPress 6 for Beef Shawarma")
        order = input("Enter your choice here:")
        if order == "1": # VEG SHAWARAMA
            print(f"You have chosen {VegShaw['item']}.")
            qty = int(input(f"\t-How many {ShawarmaList[0]}'s do you want?:"))
            temporder[ShawarmaList[0]] = [VegShaw['MRP'] , qty]
        elif order == "2": # CHICKEN SHAWARMA
            print(f"You have chosen {ChickShaw['item']}.")
            qty = int(input(f"\t-How many {ShawarmaList[1]}'s do you want?: "))
            temporder[ShawarmaList[1]] = [ChickShaw['MRP'] , qty ]
        elif order == "3": # MUTTON SHAWARMA
            print(f"You have chosen {MuttShaw['item']}.")
            qty = int(input(f"\t-How many {ShawarmaList[2]}'s do you want?: "))
            temporder[ShawarmaList[2]] = [MuttShaw['MRP'] , qty ]
        elif order == "4": # BBQ SHAWARMA
            print(f"You have chosen {BBQShaw['item']}.")
            qty = int(input(f"\t-How many {ShawarmaList[3]}'s do you want?: "))
            temporder[ShawarmaList[3]] = [BBQShaw['MRP'] , qty ]
        elif order == "5": # LEBANESE SHAWARMA
            print(f"You have chosen {LebShaw['item']}.")
            qty = int(input(f"\t-How many {ShawarmaList[4]}'s do you want?: "))
            temporder[ShawarmaList[4]] = [LebShaw['MRP'] , qty ]
        elif order == "6": # BEEF SHAWARMA
            print(f"You have chosen {BeefShaw['item']}.")
            qty = int(input(f"\t-How many {ShawarmaList[5]}'s do you want?: "))
            temporder[ShawarmaList[5]] = [BeefShaw['MRP'] , qty ]
        else:
            print("Did not recieve correct input. Please try again.")
    if billingchoice == "3": # Beverage
        print("You have chosen Beverages.")
        print(f"{Style.BRIGHT}\tPress 1 for Tea\n\tPress 2 for Coffee\n\tPress 3 for Lemonade\n\tPress 4 for Soft Drinks\n\tPress 5 for Milkshake")
        order = input("Enter your choice here: ")
        if order == "1": # TEA
            print(f"You have chosen {Tea['item']}.")
            qty = int(input(f"\t-How many cups of {BeverageList[0]} do you want?: "))
            temporder[BeverageList[0]] = [Tea['MRP'] , qty]
        elif order == "2": # COFFEE
            print(f"You have chosen {Coffee['item']}.")
            qty = int(input(f"\t-How many cups of {BeverageList[1]} do you want?: "))
            temporder[BeverageList[1]] = [Coffee['MRP'] , qty]
        elif order == "3": # LEMONADE
            print(f"You have chosen {Lemon['item']}.")
            qty = int(input(f"\t-How many glasses of {BeverageList[2]} do you want?: "))
            temporder[BeverageList[2]] = [Lemon['MRP'] , qty]
        elif order == "4": # SODA
            print(f"You have chosen {Soda['item']}.")
            qty = int(input(f"\t-How many cans of {BeverageList[3]} do you want?: "))
            temporder[BeverageList[3]] = [Soda['MRP'] , qty]
        elif order == "5": # MILKSHAKE
            print(f"You have chosen {MlkShk['item']}.")
            qty = int(input(f"\t-How many glasses of {BeverageList[4]} do you want?: "))
            temporder[BeverageList[4]] = [MlkShk['MRP'] , qty]
        else:
            print("Did not receive correct input. Please try again.")
    print(" ")
    print("Your current order is:")
    i = 1
    for itname,prqt in temporder.items():
        print(f"{Style.BRIGHT}{i}) {itname}\tx\t{prqt[1]}\t=\t{prqt[0] * prqt[1]}₹")
        i += 1
    qty = 0
    order = 0
    print(" ")
    cont = input(f"Do you want to add another item? Y/N: ")
print("\nYour current order is:")
i = 1
for itname, prqt in temporder.items():
    print(f"{Style.BRIGHT}{i}) {itname}\tx\t{prqt[1]}\t=\t{prqt[0] * prqt[1]}₹")
    i += 1
    dishes = temporder.keys()
    disheslist = list(dishes)
    priceqty = temporder.values()
    priceqtylist = list(priceqty)
delchoice = input("\nDo you want to delete an item? Y/N: ")
if delchoice == "y" or delchoice == "Y":
    delitemqty = int(input("\t-How many items do you want to delete? : "))
    for delitem in range(delitemqty):
        temporderlist = []
        for a in temporder.keys():
            temporderlist.append(a)
        num = 1
        for bruh in temporderlist:
            print(f"{num}) {bruh}")
            num += 1
        delnum = int(input("Enter the number of the item that you want to delete: "))
        delqty = int(input("Enter the quantity you want to delete: "))
        priceqtylist[delnum - 1][1] = priceqtylist[delnum - 1][1] - delqty
        if priceqtylist[delnum - 1][1] == 0:
            del priceqtylist[delnum - 1]
            del disheslist[delnum - 1]
            del temporder[temporderlist[delnum - 1]]
            del temporderlist[delnum - 1]
        print("Item deleted succesfully. Updated order is: ")
        serialnum = 1
        for p, q in temporder.items():
            print(f"{Style.BRIGHT}{serialnum})\t{p}\tx\t{q[1]}")
            serialnum += 1
elif delchoice == "n" or "N":
        print("No items will be deleted.")
else:
        print("Invalid input.")
for finalitems in range(len(disheslist)):
    finalorder[disheslist[finalitems - 1]] = priceqtylist[finalitems - 1]
print("\nYour final order is: ")
srno = 1
for forder,fprqty in finalorder.items():
    print(f"{Style.BRIGHT}{srno}) {forder}\tx\t{fprqty[1]}\t=\t{fprqty[0] * fprqty[1]}₹")
    srno +=1
totalsum = 0
for slatt in range(len(priceqtylist)):
    totalsum = totalsum + (priceqtylist[slatt][0]) * (priceqtylist[slatt][1])
print(f"{Style.BRIGHT}\nYour total bill will be:" , totalsum , "₹")
if totalsum <= 2000:
    gstper = 5
    totalsumwgst = (totalsum) +  (totalsum * gstper/100)
    print(f"\nAfter adding {(gstper)}% GST on you total bill of {totalsum}₹, your new total will be: {totalsumwgst}₹")
elif totalsum >= 2000:
    gstper = 10
    totalsumwgst = (totalsum) +  (totalsum) * (gstper/100)
    print(f"\nAfter adding {(gstper)}% GST tax on you total bill of {totalsum}₹, your new total will be: {totalsumwgst}₹")
    totalsumwgst = (totalsum) +  (totalsum) * (gstper/100)
tipchoice = input("\nWould you like to add a tip to show your appriciation? Y/N: ")
if tipchoice == "y" or tipchoice == "Y":
    tipamt = float(input(f"Thank you for tipping us! How much would you like to tip (in ₹) on a bill of {totalsumwgst}₹? :"))
    FinalPrice = totalsumwgst + tipamt
print(f"\n{Fore.LIGHTWHITE_EX}{Style.BRIGHT}This brings your to total amount to {Fore.BLUE}{FinalPrice}₹{Fore.RESET}.")
print(f"We accept Cash, Debit card, Credit card, Check, PayTm, BharatPay, Bitcoin, Ethereum and Gold.")
print(f"{Fore.LIGHTCYAN_EX}{Back.BLACK}=== Thank You for coming to our Restraunt ===")