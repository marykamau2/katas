def rev():
    mystring = input ('Enter a string to reverse\n')
    
    if " " in mystring:
        correct = mystring.split(" ")
        reversed_string = " ".join(reversed(correct))
    else:
        print(f'{mystring} is invalid!')    
rev()