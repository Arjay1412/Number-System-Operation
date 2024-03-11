# Menu 2
import Conversion as m
import Binary_Operations as bo


def binary_ops_menu():
    choice = int(input(
        "\nBinary Operations Menu:\n[1] Division\n[2] Multiplication\n[3] Subtraction"
        "\n[4] Addition\n[5] Negative (2's Complement)\n[6] Back to Main Menu\nEnter your choice (1-6): "))
    print(" ")

    if choice == 1:
        print(f"Answer: {bo.div()}")
    elif choice == 2:
        print(f"Answer: {bo.mul()}")
    elif choice == 3:
        print(f"Answer: {bo.sub()}")
    elif choice == 4:
        print(f"Answer: {bo.add()}")
    elif choice == 5:
        print(f"Answer: {bo.negation()}")
    elif choice == 6:
        main_menu()
    else:
        print("Invalid choice. Please enter a valid option.")


# Menu 3
def num_sys_conv_menu():
    choice = int(input(
        "\nNumber System Conversion Menu:, \n[1] Binary to X\n[2] Decimal to X"
        "\n[3] Octal to X\n[4] Hexa to X\nEnter your choice (1-4): "))

    if choice == 1:
        val1 = str(m.bintodec()).split(".")
        val = (float(val1[0]), float("0." + (val1[1])))
        print(f"Binary:       {m.Bin(val[0], val[1])}")
        print(f"Octal:        {m.Oct(val[0], val[1])}")
        print(f"Hexadecimal:  {m.Hex(val[0], val[1])}")
        print(f"Decimal:      {float(val[0]) + float(val[1])} \n")

    elif choice == 2:
        val = m.nums()
        print(f"Binary:       {m.Bin(val[0], val[1])}")
        print(f"Octal:        {m.Oct(val[0], val[1])}")
        print(f"Hexadecimal:  {m.Hex(val[0], val[1])}")
        print(f"Decimal:      {float(val[0]) + float(val[1])} \n")

    elif choice == 3:
        val1 = str(m.octtodec()).split(".")
        val = float(val1[0]), float("0." + (val1[1]))
        print(f"Binary:       {m.Bin(val[0], val[1])}")
        print(f"Octal:        {m.Oct(val[0], val[1])}")
        print(f"Hexadecimal:  {m.Hex(val[0], val[1])}")
        print(f"Decimal:      {float(val[0]) + float(val[1])} \n")

    elif choice == 4:
        val1 = str(m.hextodec()).split(".")
        val = float(val1[0]), float("0." + (val1[1]))
        print(f"Binary:       {m.Bin(val[0], val[1])}")
        print(f"Octal:        {m.Oct(val[0], val[1])}")
        print(f"Hexadecimal:  {m.Hex(val[0], val[1])}")
        print(f"Decimal:      {float(val[0]) + float(val[1])} \n")
    else:
        print("Invalid choice. Please enter a valid option.")


# Menu 1
def main_menu():
    print("\nMain Menu:")
    print("[1] Binary operations ")
    print("[2] Conversion ")
    print("[3] Exit")


def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            binary_ops_menu()
        elif choice == '2':
            num_sys_conv_menu()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()