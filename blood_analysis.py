# blood_analysis.py
def interface():
    print("\nMy Blood Analysis Calculator\n")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1-HDL Analysis")
        print("9-Quit")
        choice = input("\nChoose an option: ")
        if choice == '1':
            hdl_interface()
        if choice == '9':
            print("\n")
            keep_running = False


def hdl_interface():
    print("HDL Interface\n")
    pass


if __name__ == '__main__':
    interface()
