for i in range(999):
    b= input("start temp converter? \nenter y for yes and n for no :- ")
    if b=="y":
        print("write 1 for celcius")
        print("write 2 for fahrenheit")
        print("write 3 for kevin")
        print ("temprature calculator")
        x= float(input("enter the value: "))
        y= str(input("tell whether the value is in degree celcius,fahrenheit or kelvin: "))
        z= str(input("tell what you want the value to be converted to:"))
    
        if y=="1":
            if z== "1":
                print("value is: ",x)
            elif z== "2":
                print("value converted from celcius to fahrenheit is:",(x*(9/5))+32)
            elif z== "3":
                print("value converted from celcius to kelvin is: ",x+273)
            else:
                print("invalid")
    
    
        elif y=="2":
            if z== "2":
                print("value is: ",x)
            elif z== "1":
                print("value converted from fahrenheit to celcius is:",(((x-32)/9)*5))
            elif z== "3":
                print("value converted from fahrenheit to kelvin is: ",(x-32)*(1.8)+273)
            else:
                print("invalid")
        elif y=="3":
            if z== "3":
                print("value is: ",x)
            elif z== "1":
                print("value converted from kelvin to celcius is: ",x-273)
            elif z== "2":
                print("value converted from kelvin to fahrenheit is: ",(x-273)*(9/5)+32)
            else:
                print("invalid")
        
        else :
            print('invalid')  

    elif b=="n":
        print("")

    else :
        print("invalid")

    j=input("repeat the program?  \n enter y for yes, n for no :-  ")
    if j== "y":
        continue
    elif j== 'n':
        break
    else:
        print("invalid")
