import os, time, platform



def main():
    
    print("user on", platform.system(), platform.release()) 

    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Darwin":
        os.system('clear')
    else:
        return main()


    print("converter_binary_decimal_hexadecimal")
    valeur1 = input("write your value : ")
    print("[1] - binary (base 2)")
    print("[2] - decimal (ase 10)")
    print("[3] - hexadecimal (base 16)")
    base1 = int(input("what's the base of that value : "))
    base2 = int(input("in what base do you want to convert that value : "))
    

    if base2 == 1:
        
        if base1 == 1:
            print("error", valeur1, "is already a binary value")
            input ("press enter to go to menu")
            return main()
        
        elif base1 == 2:
            print(valeur1, "in binary is equal to :", bin(int(valeur1))[2::])
            input ("press enter to go to menu")
            return main()
        
        elif base1 == 3:
            print(valeur1, "in binary is equal to :", bin(int(valeur1, 16))[2::])
            input ("press enter to go to menu")
            return main()
        
        else:
            print("error, select a valid base")
            choix = input("did you want to quit ? y/n : ")

            if choix == "y":
                time.sleep(2)
                quit()
            
            elif choix == "n":
                time.sleep(2)
                return main()
            
            else:
                quit()
    
    
    elif base2 == 2:
        
        if base1 == 1:
            print(valeur1, "in decimal is equal to :", int(valeur1, 2))
            input ("press enter to go to menu")
            return main()
        
        elif base1 == 2:
            print("erreur", valeur1, "is already a decimal value")
            input ("press enter to go to menu")
            return main()
        
        elif base1 == 3:
            print(valeur1, "in decimal is equal to :", int(valeur1, 16))
            input ("press enter to go to menu")
            return main()
        
        else:
            print("error, select a valid base")
            choix = input("did you want to quit ? y/n : ")

            if choix == "y":
                time.sleep(2)
                quit()
            
            elif choix == "n":
                time.sleep(2)
                return main()
            
            else:
                quit()
    
    
    elif base2 == 3:
        
        if base1 == 1:
            print(valeur1, "in hexadecimal is equal to :", hex(int(valeur1, 2))[2::])
            input ("press enter to go to menu")
            return main()
        
        elif base1 == 2:
            print(valeur1, "in hexadecimal is equal to :", hex(int(valeur1))[2::])
            input ("press enter to go to menu")
            return main()
        
        elif base1 == 3:
            print("erreur", valeur1, "is already a hexadecimal value")
            input ("press enter to go to menu")
            return main()
        
        else:
            print("error, select a valid base")
            choix = input("did you want to quit ? y/n : ")
        
            if choix == "y":
                time.sleep(2)
                quit()
        
            elif choix == "n":
                time.sleep(2)
                return main()
            
            else:
                quit()
    
    
    else:
        print("error, select a valid base")
        choix = input("did you want to quit ? y/n : ")
        
        if choix == "y":
            time.sleep(2)
            quit()
    
        elif choix == "n":
            time.sleep(2)
            return main()
        
        else:
            quit()



main()