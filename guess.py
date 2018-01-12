def main():

    def initial():
        print("You will be playing a round in the " + category + " category. Good Luck!")

    def anim():
        initial()

    def cit():
        initial()

    def spo():
        initial()
    
    print()
    print("Hello! Welcome to Ryaan's guessing game.")
    print()
    print("After choosing a category, you will be given two clues from which you must guess" +
          "which animal, city, or sports team the hints are referring to. Each round consists " +
          "of 5 questions, each one worth 20 points. The maximum score is 100 points.")
    print()
    category = input("Please choose from the following categories: [animals, cities, sports]- ")
    print()

    if category == "animals":
        anim()

    elif category == "cities":
        cit()

    elif category == "sports":
        spo()

    else: print("Please try again and type a proper catgory from the options above.")

main()
