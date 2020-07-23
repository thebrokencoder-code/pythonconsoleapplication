import random,csv
import os.path
from os import path
import pandas

class CreateAccount:
    def __init__(acc,acc_name,acc_no,acc_type,acc_balance,userid,password):
        acc.acc_name=acc_name
        acc.acc_no=acc_no
        acc.acc_type=acc_type
        acc.acc_balance=acc_balance
        acc.userid=userid
        acc.password=password
    def newAccount(newacc):
        if(path.isfile("accounts.csv")):
            acc_details=[[newacc.acc_name,newacc.acc_no,newacc.acc_type,newacc.acc_balance,newacc.userid,newacc.password]]
            with open("accounts.csv","a",newline='') as accfile:
                datainput=csv.writer(accfile)
                datainput.writerows(acc_details)
            accfile.close()
            print("Account Created Successfully")
        else:
            header()
            
       
    

def header():
         with open("accounts.csv","w") as accfile:
            datainput=csv.writer(accfile)
            acc_attributes=['ACCNAME','ACCNO','TYPE','BALANCE','id','password']
            datainput.writerow(acc_attributes)
            
def createNewaccount():
    userid=str(input("Create a new user id =\t"))
    password=str(input("Create a new strong password for acc =\t"))
    name=str(input("Enter Account Holder Name="))
    accno="ABCBANK"+str(random.randint(101,1001))
    atype=str(input("Select Account type : 1.SAVINGS\t2.CURRENT \t 1 or 2 ="))
    balance=str(input("Set Account balance \t Minimum 1000.00rs="))
    acc=CreateAccount(name,accno,atype,balance,userid,password)
    acc.newAccount()

    
def userMode(role):
    print("Welcome user")
    print("please select an operation")
    user_op=int(input("1.Create a new account\n2.Login Into Existing account\n1 or 2="))
    if(user_op==1):
        createNewaccount()
    elif(user_op==2):
        print("\tenter login credentials")
        userid = str(input("\tenter use id="))
        password=str(input("\tEnter user password="))
        if(userid!=None):
            authFunction(userid,password,role)
        else:
            print("Enter Valid Value")
    
def authFunction(uid,password,role):
    if(role==1):
        if(path.isfile("accounts.csv")):
            with open('accounts.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                   accno=row['ACCNO']
                   if(row["id"]==uid and row["password"]==password):
                       session=True
                       userServices(uid,accno,session)
                   else:
                       print("invalid credentials")
        else:
            print("NO records contact bank admin")
    elif(role==2):
        if uid=="bala" and password=="admin":
            accountantServices()
        else:
            print("INVALID CREDENTIALS")
    else:
        return "UNAUTHORISED ACCESS"

def userServices(uid,accno,session):
    print("Welcome",uid)
    print("please select an operation\n")
    service_num=int(input("1.VIewBalance 2.AddAmount 3.WithdrawAmount \t 1or2or3= "))
    if(service_num==1):
        viewBalance(uid,accno,session)
    elif(service_num==2):
        addAmount(uid,accno,session)
    elif(service_num==3):
        withdraw(uid,accno,session)
    else:
        print("enter valid operation or exit")

#method for fetching logged user balance
def viewBalance(uid,accno,session):
    with open('accounts.csv','r') as accs:
        reader = csv.DictReader(accs)
        for row in reader:
            if(row["id"]==uid and session==True):
                balance=row['BALANCE']
                print("YOUR CURRENT BALANCE =",balance)
                print("1.return to previous menu 2.return to main menu 3.logout 1or2or3 =")
                usop=int(input())
                if usop==1:
                    userServices(uid,accno,session)
                elif usop==2:
                    userMode(1)
                elif usop==3:
                    session=False
                    bank()
            else:
                return "please login"
#method to withdraw
def withdraw(uid,accno,session):
    withdrawal_amount=int(input("Enter amount to be withdrawn ="))
    if(session):
        acc=pandas.read_csv("accounts.csv",index_col="ACCNO")
        bal=acc.at[accno,'BALANCE']
        if bal<withdrawal_amount:
            print("INSUFFICIENT FUNDS,\nAVAILABLE BALANCE =",bal)
            op=int(input("1.Try Again 2.EXIT 1or2= "))
            if(op==1):
                withdraw()
                
            elif(op==2):
                userServices()
                
            else:
                exit()
        else:
            up=bal-withdrawal_amount
            acc.at[accno,'BALANCE']=up
            acc.to_csv('accounts.csv')
            print("1.return to previous menu 2.return to main menu 3.logout 1or2or3 =")
            usop=int(input())
            if usop==1:
                userServices(uid,accno,session)
            elif usop==2:
                userMode(1)
            elif usop==3:
                session=False
                bank()
    else:
        return "LOGIN AGAIN"
        
def addAmount(uid,accno,session):
    credit_amount=int(input("Enter amount to be added ="))
    if(session):
        acc=pandas.read_csv("accounts.csv",index_col="ACCNO")
        bal=acc.at[accno,'BALANCE']
        up=bal+credit_amount
        acc.at[accno,'BALANCE']=up
        acc.to_csv('accounts.csv')
        upacc=pandas.read_csv("accounts.csv",index_col="ACCNO")
        bal=acc.at[accno,'BALANCE']
        if bal==up:
            print("Amount added Succesfully")
        else:
            print("Failed")
        print("1.return to previous menu 2.return to main menu 3.logout 1or2or3 =")
        usop=int(input())
        if usop==1:
            userServices(uid,accno,session)
        elif usop==2:
            userMode(1)
        elif usop==3:
            session=False
            bank()
    else:
        return "LOGIN AGAIN"
        
        
            
                
    
            
    

#entry point function
def bank():
    print("Welcome to ABCBANK please select mode of user")
    role = int(input("1.customer \t 2. accountant \t1 or 2="))
    if(role==1):#user role k liye 1
        userMode(role) #ye method call hoga with role value as 1
    elif(role==2):
        accountMode(role)#similar to previous method with role value as 2
    else:
        print("enter valid user mode or exit")
    


def accountantServices():
    print("Accountant Mode LOGIN SuccessFull")
    print("please select an operation")
    user_op=int(input("1.view all user accounts\n2.particular user\n 1 or 2="))
    if(user_op==1):
        viewAccounts()
    elif(user_op==2):
        viewUser()
        
def accountMode(role):
    print("\tWelcome Accountant")
    print("\tPlease login to continue")
    userid = str(input("\tenter use id="))
    password=str(input("\tEnter user password="))
    if(userid!=None):
        authFunction(userid,password,role)
    else:
        print("Enter Valid Value")
    
def viewAccounts():
    with open('accounts.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["ACCNAME"], row["ACCNO"])
        
bank()
