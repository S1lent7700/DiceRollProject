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
    parse.add_argument('-p', '--prompt', dest="wizard", action="store_true", help="Init the program with a prompt.")
    parse.add_argument('-d', '--data', dest="stat_data", action="store_true", help="Print data on current roll(s).")

    args = parse.parse_args()

    if args is None:
        print(parse.usage); exit(1)
    else:
        if args.wizard:
            console = DMW()
            console.roll_dice_consolemode(); return

        if args.dice_num:
            num = int(args.dice_num)
            # Init the class -- If the '-d'/'--data' option is triggered
            # print the dice roll data
            if args.stat_data:
                mod = DM(num, True)
                mod.roll_dice(); return
            else:
                mod = DM(num, False)
                mod.roll_dice(); return

if __name__ == '__main__':
    main()

