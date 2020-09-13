import argparse
from dicemodule import DiceModule as DM, DiceModuleWizard as DMW

'''
The main driver module.
Author: Gleb Bair
CEG 3110
'''

def main():
    # Init the parser module
    parse = argparse.ArgumentParser(usage="python3 dice.py <DICE_AMOUNT> [-w <CONSOLE>] | -h, --help", conflict_handler="resolve")
    parse.add_argument('-n', '--die-number', type=int, dest="dice_num", default=5, metavar="", help="Specify the number of dice to use (i.e: 3)")
    parse.add_argument('-t', '--times', type=int, dest="trials", default=1, metavar="", help="How many roll trials do you want?")
    parse.add_argument('-p', '--prompt', dest="wizard", action="store_true", help="Init the program with a prompt.")
    parse.add_argument('-d', '--data', dest="stat_data", action="store_true", help="Print data on current roll(s).")

    args = parse.parse_args()

    if args is None:
        print(parse.usage); exit(1)
    else:
        if args.dice_num:
            num = int(args.dice_num)
            # Init the class -- If the '-d'/'--data' option is triggered
            # print the dice roll data
            if args.stat_data:
                mod = DM(num, True)
                if args.trials:
                    pass
                else:
                    mod.roll_dice(); return
            else:
                mod = DM(num, False)
                if args.trials:
                    pass
                else:
                    mod.roll_dice(); return

        if args.wizard:
            console = DMW()
            console.roll_dice_consolemode(); return

        if args.trials:
            num2 = int(args.dice_num)
            # Print "banner"
            if int(args.trials) < 2:
                print("\nRolling", num2, "dice with",int(args.trials),"trial" + "\n" + '-' * 35 + "\n")
            else:
                print("\nRolling", num2, "dice with",int(args.trials),"trials" + "\n" + '-' * 35 + "\n")
            for i in range(0, int(args.trials)):
                mod2 = DM(num2, False)
                mod2.roll_dice()
            return

if __name__ == '__main__':
    main()

