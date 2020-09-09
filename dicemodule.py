import random

'''
This is the primary dice roll module. This module contains a reusable class
which, when initialized, will allow the user to specify how many dice that
will be rolled. For each dice (5), a number (1,6) will be selected at random
and will be displayed in descending (column) fashion.
'''

class DiceModule:

    def __init__(self, dice_num, display_data):
        self.dice = dice_num
        self.show_data = display_data
        self.dice_sides = [1, 2, 3, 4, 5, 6]
        self.dice_roll_int = []
        self.sum_result = 0


    def roll_dice(self):
        try:
            if int(self.dice) > 5:
                print("\nPlease enter a value 1-5 -- Got: ",int(self.dice), "\n"); exit(1)
            elif int(self.dice) <= 0:
                print("\nInteger value must be greater than 0 (cannot be 0 or any negative number)...\n"); exit(1)
            else:
                # Print a banner
                if self.dice > 1:
                    print("\n" + ("=" * 5) + " Rolling ",int(self.dice),"dice " + ("=" * 6))
                    pass
                else:
                    print("\n" + ("=" * 5) + " Rolling die " + ("=" * 6))
                    pass
                # Establish a loop for dice number
                for i in range(1, (self.dice + 1)):
                    result = random.choice(self.dice_sides)
                    # Append the resulting rolls to the dice roll list
                    self.dice_roll_int.append(int(result))
                    # Add the sum
                    self.sum_result = sum(self.dice_roll_int)
                    # Print the result
                    print("Dice Roll [", i, "] -- Yields: ", result)
                # Print the sum
                if self.show_data:
                    print("\n------ Roll Data -------")
                    _Core.print_sum(self.sum_result)
                    _Core.frequent(self.dice_roll_int)

                #
        except ValueError as e:
            print("\nValue must be an integer! -- " + str(e) + "\n"); exit(1)


class DiceModuleWizard:

    def __init__(self):
        self.dice_sides = [1, 2, 3, 4, 5, 6]

    def roll_dice_consolemode(self):
        # Give the user a prompt. Have the user first enter how many
        # Dice that will be used. Then, return the random rolls based
        # on the dice amount. Also, let the user specify if there is
        # range to the die faces
        while True:
            try:
                try:
                    # The prompt
                    string = input("How many dice will be used?: ")
                    # Check the input
                    if len(string) == 0:
                        # Print error -- Prompt length
                        print("\nPlease enter an integer into the prompt (value cannot be nothing)...\n")
                        # break
                        pass
                    if int(string) > 5:
                        print("\nPlease enter a value 1-5 -- Got: ",int(string),"\n")
                        pass
                    elif len(string) > 1:
                        print("\nPlease enter a single digit value (1-6)...\n")
                        pass
                    elif int(string) <= 0:
                        # Print error -- 0 or below
                        print("\nInteger value must be greater than 0 (cannot be 0 or any negative number)...\n")
                        # break
                        pass
                    #####
                    else:
                        # Roll the dice
                        for i in range(1, (int(string) + 1)):
                            result = random.choice(self.dice_sides)
                            # Print the result
                            print("Dice Roll [", i, "] -- Yields: ", result)
                except KeyboardInterrupt:
                    print("\n\nCtrl + C caught!\n"); exit(0)
            except ValueError as e:
                print("\nValue must be an integer! -- " + str(e) + "\n")

class _Core:

    def __init__(self):
        pass

    @staticmethod
    def print_sum(__sum):
        print("Total Sum: ",int(__sum)); pass

    @staticmethod
    def frequent(__list):
        counter = 0
        int_list = __list[0]

        for i in __list:
            c_freq = __list.count(i)
            if c_freq > counter:
                # Reverse
                counter = c_freq
                int_list = i
        # Print most frequent
        print("Max Value: ",int_list,"\n")