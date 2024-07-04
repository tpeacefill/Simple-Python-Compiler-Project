from typing import Optional
import tokens
from tokens import Token

class Lexer:
    def __init__(self, text: str):
        # Initialize the lexer with the input text
        self.text = text
        self.index = 0
        self.current_char: Optional[str] = None
        self.advance()

    def advance(self):
        # Advance to the next character in the input text
        if self.index < len(self.text):
            self.current_char = self.text[self.index]
            self.index += 1
        else:
            self.current_char = None

    def get_tokens(self):
        # Tokenize the entire input text and return a list of tokens
        tokens_list: list[Token] = []

        while self.current_char is not None:
            if self.current_char.isspace():
                # Skip whitespace
                self.advance()
            elif self.current_char == "\"" or self.current_char == "'":
                # Get a string token
                tokens_list.append(self.get_string())
            elif self.current_char == "." or self.current_char.isdigit():
                # Get a number token
                tokens_list.append(self.get_number())
            elif self.current_char == "+":
                # Get a plus token
                self.advance()
                tokens_list.append(Token(tokens.TT_PLUS))
            elif self.current_char == "-":
                # Get a minus token
                self.advance()
                tokens_list.append(Token(tokens.TT_MINUS))
            elif self.current_char == "*":
                # Get a multiply token
                self.advance()
                tokens_list.append(Token(tokens.TT_MULTIPLY))
            elif self.current_char == "/":
                # Get a divide token
                self.advance()
                tokens_list.append(Token(tokens.TT_DIVIDE))
            elif self.current_char == "%":
                # Get a modulo token
                self.advance()
                tokens_list.append(Token(tokens.TT_MODULO))
            elif self.current_char == "(":
                # Get a left parenthesis token
                self.advance()
                tokens_list.append(Token(tokens.TT_LPAREN))
            elif self.current_char == ")":
                # Get a right parenthesis token
                self.advance()
                tokens_list.append(Token(tokens.TT_RPAREN))
            else:
                # Raise an error for any illegal character
                raise RuntimeError("Illegal character -> " + self.current_char)

        return tokens_list

    def get_number(self):
        # Parse a number token from the input text
        number: str = self.current_char
        dot_count = 0
        self.advance()

        while self.current_char is not None and (
            self.current_char == "." or self.current_char.isdigit()
        ):
            if self.current_char == ".":
                dot_count += 1
                if dot_count > 1:
                    break

            number += self.current_char
            self.advance()

        # Handle numbers that start or end with a dot
        if number[0] == ".":
            number = "0" + number

        if number[-1] == ".":
            number += "0"

        return Token(tokens.TT_NUMBER, float(number))

    def get_string(self):
        # Parse a string token from the input text
        string = ""
        quote_type = self.current_char  # This will be either a single or double quote
        self.advance()  # Skip the opening quote

        while self.current_char is not None and self.current_char != quote_type:
            string += self.current_char
            self.advance()

        if self.current_char != quote_type:
            raise RuntimeError("Unterminated string literal")

        self.advance()  # Skip the closing quote

        return Token(tokens.TT_STRING, string)
