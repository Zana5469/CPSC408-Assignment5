
# module contains miscellaneous functions
class helper():

    # Function checks for user input given a list of choices
    @staticmethod
    def get_choice(lst):

        choice = input("\nEnter choice number: ")

        while not choice.isdigit() or int(choice) not in lst:
            print("\nIncorrect option. Try again.")
            choice = input("Enter choice number: ")

        return int(choice)

    # Function prints a list of results
    @staticmethod
    def pretty_print(lst):

        print("Results..\n")

        for i in lst:
            print(i)

        print("")
