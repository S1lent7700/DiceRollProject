import os

'''
The custom test harness for the dice program. This tests the randomness
of the outputs.
Author: Gleb Bair
CEG 3110
'''

class Harness:

    def __init__(self):
        self.default_runs = 10
        self.default_quantity = 3
        self.cwd = os.getcwd()
        self.dice_mod = "dice.py"
        self.interpreter = "python3"
        self.default_params = "-n"

    def run(self):
        # Provide the user with the prompts
        run_prompt = input("How many times should the program run? (X): ")

        try:
            if int(run_prompt) == 0 or int(run_prompt) <= 0:
                def_runs = self.default_runs
                _Core.print_setting("Number of runs", int(def_runs))
            else:
                def_runs = int(run_prompt)
                _Core.print_setting("Number of runs", int(def_runs))

            dice_prompt = input("How many dice do you want to roll? (Y): ")

            if int(dice_prompt) == 0 or int(dice_prompt) <= 0:
                dice_no = self.default_quantity
                _Core.print_setting("Number of dice to roll", int(dice_prompt))
            else:
                dice_no = int(dice_prompt)
                _Core.print_setting("Number of dice to roll", int(dice_prompt))

            _Core.print_banner("Running harness...")

            harness = Harness()
            harness._runtime(int(def_runs), int(dice_no))

        except ValueError as e:
            _Core.print_error("Vakue miss-match -> " + str(e)); exit(1)

    def _runtime(self, runs, dice):
        for i in range(0, int(runs)):
            os.system(self.interpreter + " " + self.cwd + "/" + self.dice_mod + " " + self.default_params + " " + str(dice))

class _Core:

    def __init__(self):
        pass

    @staticmethod
    def print_setting(title, setting):
        print("- " + str(title) + " -> ",setting)

    @staticmethod
    def print_banner(string):
        print(("=" * 40))
        print(string)
        print(("=" * 40))

    @staticmethod
    def print_error(*errors):
        for error in errors:
            print("[Error]: " + error)


def main():
    harness = Harness()
    harness.run()

if __name__ == '__main__':
    main()
