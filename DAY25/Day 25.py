'''
#EXCEPTION HANDLINGS:HANDLES THE RUN TIME ERRORS AND PREVENTS IT FORM CRASHING
try:
    n=10
    if n>0:
        print("+ve")
    else:
        print("-ve or 0")
except NameError:
    print("define the n")
else:
    print("no errors occured")
finally:
    print("end of the program")




try:
    n=10
    print(n)
    print(13+12)
    print(int(input("enter the int: ")))
    d={1:1,2:3,4:7}
    print(d[4])
    l=[34,456,134,3456]
    print(l[0])
    print(1/9)      
except NameError:
    print("define the n")
except TypeError:
    print("give same data types")
except ValueError:
    print("give the proper datatypes")
except KeyError:
    print("key is not present")
except IndexError:
    print("index is not there")
exceptZeroDivisonError:
    print("you cant divide with zero")
    
else:
    print("no errors occured")
finally:
    print("end of the program")



try:
    n=10
    print(n)
    print(13+12)
    print(int(input("enter the int: ")))
    d={1:1,2:3,4:7}
    print(d[4])
    l=[34,456,134,3456]
    print(l[0])
    print(1/9)      
except (NameError,ValueError,TypeError,KeyError,IndexError,ZeroDivisonError) as e:
    print("error occured :",e)
else:
    print("no errors occured")
finally:
    print("end of the program")
    




try:
    n=10
    print(n)
    print(13+12)
    print(int(input("enter the int: ")))
    d={1:1,2:3,4:7}
    print(d[4])
    l=[34,456,134,3456]
    print(l[0])
    print(1/9)      
except Exception as e:
    print("error occured :",e)
else:
    print("no errors occured")
finally:
    print("end of the program")



try:
    n=-10
    if n<0:
        raise Exception("amount needs to be >0")
except Exception as e:
    print("error occured :",e)
else:
    print("no errors occured")
finally:
    print("end of the program")

'''

#FILE OPERATIONS

































































































































































































