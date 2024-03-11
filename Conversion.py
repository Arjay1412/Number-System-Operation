
def nums():
    user_input = input("\nEnter a Number: ")
    if "." in user_input:
        user_input = user_input.split(".")
    else:
        user_input = user_input + ".0"
        user_input = user_input.split(".")

    WholeNum = float(user_input[0])
    Fraction = float("0." + (user_input[1]))

    return WholeNum, Fraction

def Bin(WholeNum, Fraction):
    WN = WholeNum
    Fr = Fraction
    Output = ""
    OutputFinal = ""

    while WN != 0:
        if WN%2 == 0:
            Output += "0"
        elif WN%2 == 1:
            Output += "1"
        WN = int(WN/2)
        if WN == 1:
            Output += "1"
            break

    for i in range(16):
        Fr = Fr * 2
        if Fr > 1 and Fr != 1:
            OutputFinal = OutputFinal + "1"
            Fr -= 1
        elif Fr == 1.0:
            OutputFinal = OutputFinal + "1"
            break
        elif Fr > 0 and Fr < 1:
            OutputFinal = OutputFinal + "0"
        elif Fr == 0.0:
            OutputFinal = OutputFinal + "0"
            break
    Output = Output[::-1]
    while len(Output)%4 != 0:
        Output = "0" + Output

    Result = (Output+"."+OutputFinal)
    return Result

def Oct(WholeNum, Fraction):
    WN = int(WholeNum)
    Fr = Fraction
    Output = ""
    OutputFinal = ""

    while WN != 0 and WN > 1:
        WN = int(WN)/8
        WN_split = str(WN).split(".")
        rem = float("0."+WN_split[1])*8
        Output += str(int(rem))

    while Fr != 0.0:
        Fr = float(Fr*8)
        Fr_split = str(Fr).split(".")
        Fr = float("0."+ Fr_split[1])
        OutputFinal += Fr_split[0]
        if len(OutputFinal) == 16:
            break
    else:
        OutputFinal += "0"

    Result = (Output[::-1]+"."+OutputFinal)
    return Result

def Hex(Wholenum, Fraction):
    WN = int(Wholenum)
    Fr = Fraction
    Output = ""
    OutputFinal = ""
    prefixes = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    while WN != 0 and WN > 1:
        WN = int(WN) / 16
        WN_split = str(WN).split(".")
        rem = float("0." + WN_split[1]) * 16
        hex_prefix = int(rem)

        if hex_prefix in prefixes:
            Output += prefixes[hex_prefix]
        else:
            Output += str(hex_prefix)

    while Fr != 0.0:
        Fr = float(Fr * 16)
        Fr_split = str(Fr).split(".")
        Fr = float("0." + Fr_split[1])
        hex_fr = int(Fr_split[0])


        if len(OutputFinal) == 16:
            break
        elif hex_fr in prefixes:
            OutputFinal += prefixes[hex_fr]
        else:
            OutputFinal += Fr_split[0]
    else:
        OutputFinal += "0"

    Result = (Output[::-1] + "." + OutputFinal)
    return Result

def bintodec():
    user_input = input("Enter a Binary: ")
    while not all(digit in "01." for digit in user_input):
        print("Invalid Binary number. Please enter a valid Binary number.")
        user_input = input("Enter a Binary: ")
    else:
        if "." in user_input:
            user_input = user_input.split(".")
        else:
            user_input = user_input + ".0"
            user_input = str(user_input).split(".")

        WholeNum = user_input[0]
        Fraction = user_input[1]
        Result = 0.0
        n = 0
        for i in WholeNum[::-1]:
            Result += float(int(i)*(2**n))
            n += 1
        n = -1
        for j in Fraction:
            Result += float(int(j)*(2**n))
            n -= 1
        return Result


def octtodec():
    user_input = input("\nEnter a Octal: ")
    while not all(digit in "01234567." for digit in user_input):
        print("Invalid octal number. Please enter a valid octal number.")
        user_input = input("\nEnter a Octal: ")

    if "." in user_input:
        user_input = user_input.split(".")
    else:
        user_input = user_input + ".0"
        user_input = str(user_input).split(".")

    WholeNum = user_input[0]
    Fraction = user_input[1]
    Result = 0.0
    n = 0
    for i in WholeNum[::-1]:
        Result += float(i)* (8 ** n)
        n += 1

    n = -1
    for j in Fraction:
        Result += float(j)* (8 ** n)
        n -= 1
    return Result

def hextodec():
    user_input = input("\nEnter a Hexadecimal: ")
    while not all(digit in "01234567ABCDEF." for digit in user_input):
        print("Invalid Hexadecimal number. Please enter a valid Hexadecimal number.")
        hextodec()
    if "." in user_input:
        user_input = user_input.split(".")
    else:
        user_input = user_input + ".0"
        user_input = user_input.split(".")

    WholeNum = user_input[0]
    Fraction = user_input[1]
    prefixes = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
                "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "0": 0}
    Result = 0
    n = 0
    for i in WholeNum[::-1]:
        Result += prefixes[str(i)] * (16 ** n)
        n += 1

    n = -1
    for j in Fraction:
        Result += prefixes[str(j)] * (16 ** n)
        n -= 1

    return float(Result)






