# blood_analysis.py


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
    hdl_result = hdl_input.split('=')
    hdl_category = hdl_analysis(int(hdl_result[1]))
    print(hdl_category)


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


def interface():
    print("\nMy Blood Analysis Calculator\n")
    keep_running = True
    while keep_running:
        print("\nOptions:")
        print("1-HDL Analysis")
        print("2-LDL Analysis")
        print("9-Quit")
        choice = input("\nChoose an option: ")
        if choice == '1':
            hdl_interface()
        if choice == '2':
            ldl_interface()
        if choice == '9':
            print("\n")
            keep_running = False


if __name__ == '__main__':
    interface()
