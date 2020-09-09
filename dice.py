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
    parse.add_argument('-w', '--wizard', dest="wizard", action="store_true", help="Init the program with a prompt wizard.")

    args = parse.parse_args()

    if args is None:
        print(parse.usage); exit(1)
    else:
        if args.wizard:
            console = DMW()
            console.roll_dice_consolemode(); return

        if args.dice_num:
            num = int(args.dice_num)
            # Init the class
            mod = DM(num)
            mod.roll_dice(); return

if __name__ == '__main__':
    main()

