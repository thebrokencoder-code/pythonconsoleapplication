import random,csv
import os.path
from os import path
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
            with open("accounts.csv","a") as accfile:
                datainput=csv.writer(accfile)
                datainput.writerows(acc_details)
            accfile.close()
            print("Account Created Successfully")
        else:
            header()
            
       
    def header():
         with open("accounts.csv","w") as accfile:
            datainput=csv.writer(accfile)
            acc_attributes=['ACCNAME','ACCNO','TYPE','BALANCE','UserId','PassWord']
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
    user_op=int(input("1.Create a new account\n2.Login Into Existing account\n1 or 2=\t"))
    if(user_op==1):
        createNewaccount()
    elif(user_op==2):
        print("enter login credentials")
        userid = str(input("enter use id=\t"))
        password=str(input("Enter user password=\t"))
        if(userid!=None):
            authFunction(userid,password,role)
        else:
            print("Enter Valid Value")
    
def authFunction(uid,password,role):
    if(role==1):
        accountDetails=""
        if(path.isfile("accounts.csv")):
            accfile = open("accounts.csv","r")
            print(accfile.readlines())
        else:
            print("NO records contact bank admin")
    elif(role==2):
        if uid=="bala" and password=="admin":
            accountantServices()
        else:
            print("INVALID CREDENTIALS")

def userServices():
    print("please select an operation\n")
    service_num=int(input("\t 1.VIewBalance 2.AddAmount 3.WithdrawAmount \t 1or2or3= "))
    if(service_num==1):
        viewBalance()
    elif(service_num==2):
        addAmount()
    elif(service_num==3):
        withdraw()
    else:
        print("enter valid operation or exit")
#main method hai yeh bank() call karne pe role enter karna hai
def bank():
    print("Welcome to ABCBANK please select mode of user")
    role = int(input("1.customer \t 2. accountant \t1 or 2"))
    if(role==1):#user role k liye 1
        userMode(role) #ye method call hoga with role value as 1
    elif(role==2):
        accountMode(role)#similar to previous method with role value as 2
    else:
        print("enter valid user mode or exit")
    


def accountantServices():
    print("Accountant Mode LOGIN SuccessFull")
    print("please select an operation")
    user_op=int(input("1.view all user accounts\n2.particular user\n 1 or 2=\t"))
    if(user_op==1):
        viewAccounts()
    elif(user_op==2):
        viewUser()
        
def accountMode(role):
    print("Welcome Accountant")
    print("Please login to continue")
    userid = str(input("enter use id=\t"))
    password=str(input("Enter user password=\t"))
    if(userid!=None):
        authFunction(userid,password,role)
    else:
        print("Enter Valid Value")
    
def viewAccounts():
    accs=open("accounts.csv","r")
    records=accs.readlines()
    c=0
    for record in records:
        print(record)
        c+=1
        
bank()
