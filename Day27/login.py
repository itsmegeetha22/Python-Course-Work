Try AI directly in your favourite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for ₹1,950 ₹489 for 3 months
1
100%
data = {
    123456:{'pin':1234,'balance':5000,'name':'Charan','history':[]},
    234561:{'pin':1234,'balance':8000,'name':'Pavitra','history':[]},
    345621:{'pin':1234,'balance':7000,'name':'Sreeja','history':[]},
    }

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))

    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successful")
        return True

    else:
        print("Login Failed. Try Again!!!")
        return False

def menu():
    print()
    print('[D]eposit')
    print('[W]ithdraw')
    print('[C]heck Balance')
    print('[V]iew Transactions')
    print('[E]xit')


def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]["balance"]+=amount
    print(f"{amount} is deposited successfully")
    data[acc_num]["history"].append(f"{amount} is deposited")

def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"]-=amount
        print(f"{amount} is withdraw successfully")
        data[acc_num]["history"].append(f"{amount} is withdraw")
    else:
        print("Insuffient Balance")

def checkBalance():
    print(f'Current Balance: {data[acc_num]["balance"]}')

def viewTrasactions():
    if data[acc_num]["history"]:
        print("----Transaction History----")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("----End of Transactions----")
    else:
        print("No Transactions")


















    
