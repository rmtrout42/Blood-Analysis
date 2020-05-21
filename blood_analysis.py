# blood_analysis.py


def verify_hdl_entry(entry):
    if entry.startswith('HDL'):
        return True
    else:
        return False


def hdl_analysis(hdl_result):
    if hdl_result >= 60:
        return "Good"
    elif 40 <= hdl_result < 60:
        return "Borderline"
    else:
        return "Bad"


def hdl_interface():
    # Input should be HDL = 66
    print("HDL Interface\n")
    print("Please input the result in the following format:")
    print(" HDL=##, where ## is the numeric result.")
    hdl_input = input("Result: ")
    if verify_hdl_entry(hdl_input):
        hdl_result = hdl_input.split('=')
        hdl_category = hdl_analysis(int(hdl_result[1]))
        print(hdl_category)
    else:
        print("Invalid input format\n")


def ldl_analysis(ldl_result):
    if ldl_result < 130:
        return "Normal"
    elif 130 <= ldl_result < 159:
        return "Borderline high"
    elif 160 <= ldl_result < 189:
        return "High"
    else:
        return "Very high"


def ldl_interface():
    # Input should be HDL = 66
    print("LDL Interface\n")
    print("Please input the result in the following format:")
    print(" LDL=###, where ### is the numeric result.")
    ldl_input = input("Result: ")
    ldl_result = ldl_input.split('=')
    ldl_category = ldl_analysis(int(ldl_result[1]))
    print(ldl_category)


def chol_analysis(chol_result):
    if chol_result < 200:
        return "Normal"
    elif 200 <= chol_result < 239:
        return "Borderline high"
    else:
        return "High"


def chol_interface():
    # Input should be HDL = 66
    print("Cholesterol Interface\n")
    print("Please input the result in the following format:")
    print(" Chol=###, where ### is the numeric result.")
    chol_input = input("Result: ")
    chol_result = chol_input.split('=')
    chol_category = chol_analysis(int(chol_result[1]))
    print(chol_category)


def interface():
    print("\nMy Blood Analysis Calculator\n")
    keep_running = True
    while keep_running:
        print("\nOptions:")
        print("1-HDL Analysis")
        print("2-LDL Analysis")
        print("3-Cholesterol Analysis")
        print("9-Quit")
        choice = input("\nChoose an option: ")
        if choice == '1':
            hdl_interface()
        if choice == '2':
            ldl_interface()
        if choice == '3':
            chol_interface()
        if choice == '9':
            print("\n")
            keep_running = False


if __name__ == '__main__':
    interface()
