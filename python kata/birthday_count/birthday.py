def main():
    bdays={"newt":"18/12/1802","diana":"13/02/2005"} 
    print(bdays.keys)
    name=input("enter a username")
    if bdays[name]:
       print(bdays[name])
    else:
        print("there is no such username")