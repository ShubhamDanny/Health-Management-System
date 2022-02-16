
def getdate():
    import datetime
    return datetime.datetime.now()

ret_or_log = int(input("what you want to do: retrive(1) or log(2): "))

def log():
    name = int(input("Enter your name: shubham(1), mandeep(2), abhya(3): "))

    if name == 1:
        di_or_ex = int(input("What you want to retrive: Diet(1) or Exercise(2): "))

        if di_or_ex == 1:
            with open('s_diet.txt') as f:
                print(f.read())
        elif di_or_ex == 2 :
            with open('s_ex.txt') as f:
                print(f.read())
        else:
            print("SyntaxError")
        
    elif name == 2:
        di_or_ex = int(input("What you want to log: Diet(1) or Exercise(2): "))

        if di_or_ex == 1:
            with open('m_diet.txt') as f:
                print(f.read())
        elif di_or_ex == 2 :
            with open('m_ex.txt') as f:
                print(f.read())
        else:
            print("SyntaxError")

    elif name == 3:
        di_or_ex = int(input("What you want to log: Diet(1) or Exercise(2): "))

        if di_or_ex == 1 :
            with open('a_diet.txt') as f:
                print(f.read())
        elif di_or_ex == 2 :
            with open('a_ex.txt') as f:
                print(f.read())
        else:
            print("SyntaxError")


def ret():
    name = int(input("Enter your name: shubham(1), mandeep(2), abhya(3): "))

    if name == 1:
        di_or_ex = int(input("What you want to log: Diet(1) or Exercise(2): "))

        if di_or_ex == 1:
            time = getdate()
            log = input("what did you ate: ")
            with open('s_diet.txt', "a") as f:
                f.write(f"[{time}]- {log}\n" )
            print("Item added succesfully!")
                
        elif di_or_ex == 2 :
            time = getdate()
            diet = input("what did you exercised: ")
            with open('s_ex.txt', "a") as f:
                f.write(f"[{time}]- {diet}\n")
            print("Item added succesfully!")

        else:
            print("SyntaxError")
        
    elif name == 2:
        di_or_ex = int(input("What you want to log: Diet(1) or Exercise(2): "))

        if di_or_ex == 1:
            time = getdate()
            log = input("what did you ate: ")
            with open('m_diet.txt', "a") as f:
                f.write(f"[{time}]- {log}\n" )
            print("Item added succesfully!")

        elif di_or_ex == 2 :
            time = getdate()
            diet = input("what did you exercised: ")
            with open('m_ex.txt', "a") as f:
                f.write(f"[{time}]- {diet}\n")
            print("Item added succesfully!")

        else:
            print("SyntaxError")

    elif name == 3:
        di_or_ex = int(input("What you want to log: Diet(1) or Exercise(2): "))

        if di_or_ex == 1:
            time = getdate()
            log = input("what did you ate: ")
            with open('a_diet.txt', "a") as f:
                f.write(f"[{time}]- {log}\n" )
            print("Item added succesfully!")

        elif di_or_ex == 2 :
            time = getdate()
            diet = input("what did you exercised: ")
            with open('a_ex.txt', "a") as f:
                f.write(f"[{time}]- {diet}\n")
            print("Item added succesfully!")
            
        else:
            print("SyntaxError")

    else:
        print("SyntaxError")


