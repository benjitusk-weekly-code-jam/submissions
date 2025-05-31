# Week 1: Basic Calculator
# Author: Benji Tusk
from calculator import Calculator


def main():
    """Entry point for the basic calculator program."""
    my_calc = Calculator()
    try:
        my_calc.calculate()

        if my_calc.result is not None:
            print(f"{my_calc.expression} = {my_calc.result}")
        else:
            raise ValueError("No result calculated.")
    except ZeroDivisionError:
        print(f"Woah there! You can't divide by zero!")
    except ValueError:
        print(f"Unfortunately, an unexpected error occurred.")
    except Exception:
        print(f"An error occurred. Please check your input and try again.")


if __name__ == "__main__":
    main()
