def main():
    number = int(input("How many quick picks? "))
    while number < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    import random
    for i in range(number):
        quick_pick = []
        for j in range(6):
            pick_number = random.randint(1,45)
            while number in quick_pick:
                number = random.randint(1,45)
            quick_pick.append(pick_number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()

