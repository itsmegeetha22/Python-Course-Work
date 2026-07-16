Try AI directly in your favourite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for ₹1,950 ₹489 for 3 months
1
100%
import logic as lg

if lg.login():
    print("Welcome to ATM")

    while True:
        lg.menu()   
        ch = input("Enter your choice: ").upper()
        if ch=='D':
            lg.deposit()
        elif ch=='W':
            lg.withdraw()
        elif ch=='C':
            lg.checkBalance()
        elif ch=='V':
            lg.viewTrasactions()
        elif ch=='E':
            print("Thankyou")
            break
        else:
            print("Invalid Input")
    
