import tokens

class NumberNode:
    def __init__(self, value: float):
        # Initialize a NumberNode with a floating point value
        self.value = value

    def __repr__(self) -> str:
        # Return a string representation of the number node
        return str(self.value)


class StringNode:
    def __init__(self, value: str):
        # Initialize a StringNode with a string value
        self.value = value

    def __repr__(self) -> str:
        # Return a string representation of the string node with quotes
        return f'"{self.value}"'


class BinaryNode:
    def __init__(self, type: str, left_node, right_node):
        # Initialize a BinaryNode with a type and two child nodes (left and right)
        self.type = type
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self) -> str:
        # Return a string representation of the binary node in the form (left operator right)
        return (
            "("
            + str(self.left_node)
            + tokens.operator_to_character(self.type)
            + str(self.right_node)
            + ")"
        )


class UnaryNode:
    def __init__(self, type: str, node):
        # Initialize a UnaryNode with a type and one child node
        self.type = type
        self.node = node

    def __repr__(self) -> str:
        # Return a string representation of the unary node in the form (operator node)
        return "(" + tokens.operator_to_character(self.type) + str(self.node) + ")"
