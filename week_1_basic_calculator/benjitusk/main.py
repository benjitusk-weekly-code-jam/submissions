# Week 1: Basic Calculator
# Author: Benji Tusk
from calculator import Calculator


def main():
    """Entry point for the basic calculator program."""
    my_calc = Calculator()
    my_calc.calculate()

    if my_calc.result is not None:
        print(f"{my_calc.expression} = {my_calc.result}")
    else:
        print("No result was calculated. Sorry :(")


if __name__ == "__main__":
    main()
