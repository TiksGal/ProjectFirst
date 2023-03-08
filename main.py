import logging
from typing import Union
from calculator_module import Calculator, ScientificCalculator
import art

logging.basicConfig(filename="calculator.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

def show_operations(calculate: Union[Calculator, ScientificCalculator]) -> None:
    print(f"Available operations for {type(calculate).__name__}: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    if isinstance(calculate, ScientificCalculator):
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")

def get_input(prompt: str, input_type: type = float) -> Union[int, float]:
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except Exception as e:
            logging.error("Invalid user input: " + str(e))
            print("Invalid input, please try again.")

def perform_operation(calculate: Union[Calculator, ScientificCalculator], operation: int) -> None:
    while operation < 1 or (operation > 4 and not isinstance(calculate, ScientificCalculator)) or (operation > 9 and isinstance(calculate, ScientificCalculator)):
        logging.error("Invalid operation selected.")
        print("Invalid operation selected, please try again.")
        operation = get_input("Enter operation number: ")

    operations = {
    1: calculate.add,
    2: calculate.subtract,
    3: calculate.multiply,
    4: calculate.divide,
    5: calculate.power if isinstance(calculate, ScientificCalculator) else None,
    6: calculate.sqrt if isinstance(calculate, ScientificCalculator) else None,
    7: calculate.sin if isinstance(calculate, ScientificCalculator) else None,
    8: calculate.cos if isinstance(calculate, ScientificCalculator) else None,
    9: calculate.tan if isinstance(calculate, ScientificCalculator) else None
    }

    operation_func = operations.get(operation)
    if operation_func:
        try:
            result = operation_func()
            logging.info(f"Result of: {result}")
            print(f"Result: {result}")
        except ValueError as e:
            logging.error(str(e))
            print(str(e))
    else:
        print("Invalid operation selected.")  

def main() -> None:
    logging.info("Program started.")
    while True:
        try:
            # print("Number Cruncher")
            print(text2art("Number Cruncher", font="rnd-large"))
            print("Select a calculator:")
            print("1. Basic Calculator")
            print("2. Scientific Calculator")
            print("3. Quit")
            calc_type = get_input("Enter calculator type: ")
            choice = calc_type
            if choice == 1:
                num1 = get_input("Enter first number: ")
                num2 = get_input("Enter second number: ")
                calc = Calculator(num1, num2)
            elif choice == 2:
                num1 = get_input("Enter first number: ")
                num2 = get_input("Enter second number: ")
                calc = ScientificCalculator(num1, num2)
            elif choice == 3:
                logging.info("Programe ended.")
                print("Goodbye!")
                return
            else:
                print("Invalid calculator type selected, please try again.")
                logging.error("Invalid calculator type selected.")
                continue
            try:
                show_operations(calc)
            except UnboundLocalError:
                print("Error: Calculator variable not assigned.")
                logging.error("Unallocated calculation type")
                continue
            operation = get_input("Enter operation number: ")
            perform_operation(calc, operation)
        except Exception as e:
            print("An error occurred, please try again.")
            logging.exception("An error occurred: " + str(e))

if __name__ == "__main__":
    main()