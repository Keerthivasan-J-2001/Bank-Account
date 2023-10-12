from Validate import *
class BankAcc:
    BankName = "SBI"
    IFSC = "SBI0001090"
    def __init__(self,AcNo,name,age,gen,dob,address,city,AccType,bal,panno,Ano):
        self.AcNo = AcNo
        self.name = name
        self.age = age
        self.gen = gen
        self.dob = dob
        self.address = address
        self.city = city
        self.AccType = AccType
        self.bal = bal
        self.panno = panno
        self.Ano = Ano
    
    def display(s):
        print(s.BankName," ",s.IFSC," ",s.AcNo," ",s.name," ",s.age," ",s.address," ",
        s.city," ",s.bal," ",s.AccType," ",s.panno)
    
AccDict = {}
print("-----------------Welcome to SBI Bank-------------------------")
print("Enter 1 for Creating account")
print("Enter 2 for Displaying accounts")
print("Enter 3 for Deleting Account")
print("Enter 4 for Updation of Account Details")
print("Enter 5 for Deposit")
print("Enter 6 for Withdraw")
print("Enter 7 for Fund Transfer")
print("Enter 8 for Searching account Details")
print("Enter 9 for Viewing account balance")
print("Enter 10 for Checking credit card eligibility")
print("Enter any key to exit")

while True:
    ch = input("Enter ur choice : ")
    if ch == '1':
        AcNo = input("Enter Account Number ")
        while True:
            if AcNo_Val(AcNo):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                AcNo = input("Enter Account Number ")
        name = input("Enter Name ")
        while True:
            if AccHolder_Val(name):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                name = input("Enter Name ")
        age = input("Enter Age ")
        while True:
            if Age_Val(age):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                age = input("Enter Age ")
        gen = input("Enter Gender(Male/Female) ")
        while True:
            if Gender_Val(gen):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                gen = input("Enter Gender(Male/Female) ")
        dob = input("Enter DOB ")
        while True:
            if DOB_Val(dob):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                dob = input("Enter DOB ")
        address = input("Enter address ")
        city = input("Enter City ")
        while True:
            if City_Val(city):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                city = input("Enter City ")
        AccType = input("Enter Account type ")
        while True:
            if AccType_Val(AccType):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                AccType = input("Enter Account type ")
        bal = float(input("Enter initial Deposit "))
        while True:
            if(Bal_Val(bal)):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                bal = float(input("Enter initial Deposit "))
        panno = input("Enter PAN number ")
        while True:
            if PanCard_Val(panno):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                panno = input("Enter PAN number ")
        Ano = input("Enter Aadhaar number ")
        while True:
            if Aadhaar_Val(Ano):
                break
            else:
                print("Invalid Data Entered!! Please enter it again")
                Ano = input("Enter Aadhaar number ")
        if AcNo in AccDict.keys():
            print("Account number is already present. Duplicate value is not allowed")
        else:
            obj = BankAcc(AcNo,name,age,gen,dob,address,city,AccType,bal,panno,Ano)
            AccDict[AcNo] = obj

    elif ch == '2':
        for k,v in AccDict.items():
            v.display()

    elif ch == '3':
        print("Enter A to delete account by Account number")
        print("Enter B to delete account by Account Holder Name")
        opt = input("Enter an Option ")
        
        if opt == 'A':
            AcNo = input("Enter account number ")
            f=0
            for k,v in AccDict.items():
                if v.AcNo == AcNo:
                    del AccDict[k]
                    print("Account Deleted")
                    f=1
                    break
            if f==0 :
                print("Account number not found!!")
        
        elif opt == 'B':
            name = input("Enter name ")
            f=0
            for k,v in AccDict.items():
                if v.name == name:
                    del AccDict[k]
                    print("Account Deleted")
                    f=1
                    break
            if f==0:
                print("Name not found!!")
    
    elif ch == '4':
        AcNo = input("Enter account number to update details ")
        print("Enter A to update name ")
        print("Enter B to update address ")
        print("Enter C to update DOB")
        opt = input("Enter an Option ")
        
        if opt == 'A':
            f=0
            for k,v in AccDict.items():
                if k == AcNo:
                    f=1
                    name = input("Enter the name to be updated")
                    while True:
                        if AccHolder_Val(name):
                            v.name = name
                            print("Details Updated")
                            break
                        else:
                            print("Invalid Data Entered!! Please enter it again")
                            name = input("Enter Name ")
            if f==0 :
                print("Account number not found!!")
        elif opt == 'B':
            f=0
            for k,v in AccDict.items():
                if k == AcNo:
                    v.address = input("Enter the address to be updated")
                    print("Details Updated")
                    f=1
                    break
            if f==0 :
                print("Account number not found!!")
        elif opt == 'C':
            f=0
            for k,v in AccDict.items():
                if k == AcNo:
                    f=1
                    dob = input("Enter DOB to be updated ")
                    while True:
                        if DOB_Val(dob):
                            v.dob = dob
                            print("Details Updated")
                            break
                        else:
                            print("Invalid Data Entered!! Please enter it again")
                            dob = input("Enter DOB ")
            if f==0 :
                print("Account number not found!!")
    elif ch == '5':
        AcNo = input("Enter account number to deposit ")
        amt = int(input("Enter amount to deposit"))
        f=0
        for k,v in AccDict.items():
            if k == AcNo:
                v.bal = v.bal + amt
                print("Amount Deposited")
                f=1
        if f==0:
            print("Account number not found!!")

    elif ch == '6':
        AcNo = input("Enter account number to withdraw ")
        amt = int(input("Enter amount to withdraw"))
        f=0
        for k,v in AccDict.items():
            if k == AcNo:
                f=1
                if(v.bal > amt):
                    v.bal = v.bal - amt
                    print("Amount Withdrawn")
                else:
                    print("Insufficient Balance!!")
        if f==0:
            print("Account number not found!!")
    
    elif ch == '7':
        while True:
            AcNo1 = input("Enter your account number ")
            if(AcNo1 not in AccDict.keys()):
                print("Invalid account number!!")
                AcNo1 = input("Enter correct account number ")
            else:
                break
        while True:
            AcNo2 = input("Enter the account number that u want to send money ")
            if(AcNo2 not in AccDict.keys()):
                print("Invalid account number!!")
                AcNo2 = input("Enter correct account number ")
            else:
                break
        amt = int(input("Enter amount to be transferred"))
        for k,v in AccDict.items():
            if k == AcNo1:
                if(v.bal > amt):
                    v.bal = v.bal - amt
                    print("Amount Sent")
                else:
                    print("Insufficient Balance!!")
            if k == AcNo2:
                v.bal = v.bal + amt
                print("Amount Recieved")
    
    elif ch == '8':
        print("Enter A to search by account number")
        print("Enter B to search by name")
        print("Enter C to search by account type")
        opt = input("Enter ur option : ")
        
        if opt == 'A':
            AcNo = input("Enter account number for which details is to be displayed : ")
            f=0
            for k,v in AccDict.items():
                if k == AcNo:
                    v.display()
                    f=1
            if(f==0):
                print("No such account number!!")
        
        elif opt == 'B':
            name = input("Enter name for which details is to be displayed : ")
            f=0
            for k,v in AccDict.items():
                if v.name == name:
                    v.display()
                    f=1
            if(f==0):
                print("No such name!!")
        
        elif opt == 'C':
            AccType = input("Enter account type for which details is to be displayed : ")
            f=0
            for k,v in AccDict.items():
                if v.AccType == AccType:
                    v.display()
                    f=1
            if(f==0):
                print("No such account type!!")
        
    elif ch == '9':
        AcNo = input("Enter account number for which balance is to be displayed : ")
        f=0
        for k,v in AccDict.items():
            if k == AcNo:
                print("Balance : ",v.bal)
                f=1
        if f==0 :
            print("No such account number")
    
    elif ch == '10':
        AcNo = input("Enter account number to check eligibility : ")
        f=0
        for k,v in AccDict.items():
            if k == AcNo:
                f=1
                if(v.bal >= 20000 and int(v.age) >= 18):
                    print("Congratulations!! You are eligible to apply for credit card.")
                else:
                    print("Sorry!! You are not eligible to apply for credit card.")
        if(f==0):
                print("No such account number!!")
    else:
        break
