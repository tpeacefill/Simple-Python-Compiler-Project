from lexer import Lexer
from parser_ import Parser
from compiler import Interpreter
from values import Number

def evaluate_expression(expression):
    lexer = Lexer(expression)
    tokens = lexer.get_tokens()
    
    # Print the tokens for debugging purposes
    print("Tokens:", tokens)
    
    parser = Parser(tokens)
    ast = parser.parse()
    interpreter = Interpreter()
    result = interpreter.visit(ast)
    return result

def main():
    print("Welcome to the Personal Information Program!")

    try:
        # Collect user inputs
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))  # Ensure age is treated as an integer
        intro = input("Enter a brief introduction about yourself: ")

        # Calculate age in 5 years
        age_in_5_years = age + 5

        # Constructing the output format
        expressions = [
            f'"Name: " + "{name}"',
            f'"Current Age: " + "{str(age)}"',  # Convert age to string for concatenation
            f'"Age in 5 Years: " + "{str(age_in_5_years)}"',  # Convert age_in_5_years to string
            f'"Introduction: " + "{intro}"'
        ]

        print("\n--- Personal Information ---")
        for expression in expressions:
            print(f"Evaluating expression: {expression}")
            result = evaluate_expression(expression)
            if isinstance(result, Number):
                print(result.value)
            else:
                print(result)  # Handle strings or other types
        print("----------------------------\n")

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    main()
