import Conversion as m

def nums():
    num1 = input("\nEnter First Binary: ")
    if "." in num1:
        num1 = num1.split(".")
    else:
        num1 = num1 + ".0"
        num1 = num1.split(".")
    num2 = input("Enter Second Binary: ")
    if "." in num2:
        num2 = num2.split(".")
    else:
        num2 = num2 + ".0"
        num2 = num2.split(".")

    num1Wn = num1[0]
    num2Wn = num2[0]
    num1Fr = num1[1]
    num2Fr = num2[1]


    if len(num1Wn) > len(num2Wn):
        num2Wn = str((len(num1Wn)-len(num2Wn)) * "0") + str(num2Wn)
    elif len(num2Wn) > len(num1Wn):
        num1Wn = str((len(num2Wn) - len(num1Wn)) * "0") + str(num1Wn)
    if len(num1Fr) > len(num2Fr):
        num2Fr = str(num2Fr) + str((len(num1Fr)-len(num2Fr)) * "0")
    elif len(num2Fr) > len(num1Fr):
        num1Fr = str(num1Fr) + str((len(num2Fr) - len(num1Fr)) * "0")

    return num1Wn, num1Fr, num2Wn, num2Fr

def add():
    val = nums()
    num1Wn = val[0]
    num2Wn = val[2]
    num1Fr = val[1]
    num2Fr = val[3]
    resultWn = ""

    num1Wn += num1Fr
    num2Wn += num2Fr


    n = -1
    j = 0
    for i in num1Wn[::-1]:
        if i == "0" and i == num2Wn[n] and j == 0:
            resultWn += "0"
        elif i == "0" and i == num2Wn[n] and j == 1:
            resultWn += "1"
            j -= 1
        elif i == "0" and i == num2Wn[n] and j == 2:
            resultWn += "0"
            j -= 1
        elif i == "0" and i == num2Wn[n] and j == 3:
            resultWn += "1"
            j -= 2
        elif i == "0" and i != num2Wn[n] and j == 0:
            resultWn += "1"
        elif i == "0" and i != num2Wn[n] and j == 1:
            resultWn += "0"
        elif i == "0" and i != num2Wn[n] and j == 2:
            resultWn += "1"
            j -= 1
        elif i == "1" and i == num2Wn[n] and j == 0:
            resultWn += "0"
            j += 1
        elif i == "1" and i == num2Wn[n] and j == 1:
            resultWn += "1"
        elif i == "1" and i == num2Wn[n] and j == 2:
            resultWn += "0"
        elif i == "1" and i == num2Wn[n] and j == 3:
            resultWn += "1"
            j -= 1
        elif i == "1" and i != num2Wn[n] and j == 0:
            resultWn += "1"
        elif i == "1" and i != num2Wn[n] and j == 1:
            resultWn += "0"
        elif i == "1" and i != num2Wn[n] and j == 2:
            resultWn += "1"
            j -=1
        elif i == "1" and i != num2Wn[n] and j == 3:
            resultWn += "0"
            j -=1
        n += -1
    while j != 0:
        if j == 1:
            resultWn += "1"
            j -= 1
        elif j == 2:
            resultWn += "10"
            j -= 2
        elif j == 3:
            resultWn += "11"
            j-=3

    resultFr = resultWn[:len(num1Fr)] + "."
    resultWn = resultWn[len(num1Fr):]
    finalResult = resultWn[::-1] + resultFr[::-1]

    return finalResult

def sub():
    val = nums()
    num1Wn = val[0]
    num2Wn = val[2]
    num1Fr = val[1]
    num2Fr = val[3]
    
    num1Wn += num1Fr
    num2Wn += num2Fr

    max_len = max(len(num1Wn), len(num2Wn))

    result = ''
    borrow = 0

    for i in range(max_len-1, -1, -1):
        digit1 = int(num1Wn[i])
        digit2 = int(num2Wn[i])
        if digit1 - borrow >= digit2:
            result = str(digit1 - digit2 - borrow) + result
            borrow = 0
        else:
            result = str(digit1 + 2 - digit2 - borrow) + result
            borrow = 1

    result = result[::-1]
    resultFr = "." + result[:len(num1Fr)]
    resultWn = result[len(num1Fr):]
    finalResult = resultWn[::-1] + resultFr
    

    return finalResult

def mul():
    num1 = m.bintodec()
    num2 = m.bintodec()
    prod = str(float(num1*num2)).split(".")
    result = m.Bin(float(prod[0]), float("0." + prod[1]))
    print(f"{num1} x {num2} = {num1*num2}")
    return result

def div():
    num1 = m.bintodec()
    num2 = m.bintodec()
    qou = str(float(num1 / num2)).split(".")
    result = m.Bin(float(qou[0]), float("0." + qou[1]))
    print(f"{num1} ÷ {num2} = {num1/num2}")
    return result

def negation():
    user_input = input("\nEnter a Positive Number: ")
    while not all(digit in "0123456789." for digit in user_input):
        print("Invalid Input. Please enter a valid Positive Number.")
        negation()
    if "." in user_input:
        user_input = user_input.split(".")
    else:
        user_input = user_input + ".0"
        user_input = user_input.split(".")

    WholeNum = float(user_input[0])
    Fraction = float("0." + (user_input[1]))

    wnbin = (m.Bin(WholeNum, Fraction)).split(".")
    wnbin1 = wnbin[0]
    result = ""
    for i in wnbin1[::-1]:
        if i == "1":
            result = "1" + result
            for j in range(wnbin1[::-1].index("1")+1, len(wnbin1)):
                if wnbin1[::-1][j] == "1":
                    result = "0" + result
                else:
                    result = "1" + result
            break
        else:
            result = "0" + result
    while len(result)%4 != 0:
        result = "1" + result
    else:
        result = "1111" + result

    final_result = result + "." + wnbin[1]

    print(f"{WholeNum+Fraction} = {m.Bin(WholeNum, Fraction)}")
    print(f"2's Complemented:\n-{WholeNum+Fraction} = {result}.{wnbin[1]}")

    return final_result

