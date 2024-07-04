class Number:
    def __init__(self, value: float):
        # Initialize a Number object with a floating point value
        self.value = value

    def __repr__(self) -> str:
        # Return a string representation of the number
        return str(self.value)


class String:
    def __init__(self, value: str):
        # Initialize a String object with a string value
        self.value = value

    def __repr__(self) -> str:
        # Return the string value
        return self.value
