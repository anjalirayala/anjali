from datetime import datetime

name=input("Enter Your Name:")
# list of items
lists="""
Rice Rs    20/kg
Sugar Rs   30/kg
salt Rs    20/kg
oil Rs     80/liter
paneer Rs  110/kg
Maggie Rs  50/kg
Boost Rs   90/each
colgate Rs 85/each
"""
# decleration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

# rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':80,
'panner':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item]) # rice*quantity
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered is not availabel")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","anjali supermarket",25*"=")
            print(28*" ","guntakal")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print(7*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ",'Thanks for visiting')
            print(75*"-")











