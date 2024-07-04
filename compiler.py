from nodes import *
from values import Number, String
import tokens

class Interpreter:
    def __init__(self):
        # Initialize the interpreter
        pass

    def visit(self, node):
        # Dispatch method to visit the appropriate node type
        if isinstance(node, BinaryNode):
            return self.visit_binary_node(node)
        elif isinstance(node, UnaryNode):
            return self.visit_unary_node(node)
        elif isinstance(node, NumberNode):
            return Number(node.value)
        elif isinstance(node, StringNode):
            return String(node.value)
        else:
            raise RuntimeError("Unknown node")

    def visit_binary_node(self, node: BinaryNode):
        # Visit a binary node and perform the appropriate binary operation
        if node.type == tokens.TT_PLUS:
            left = self.visit(node.left_node)
            right = self.visit(node.right_node)
            if isinstance(left, Number) and isinstance(right, Number):
                return Number(left.value + right.value)
            elif isinstance(left, String) and isinstance(right, String):
                return String(left.value + right.value)
            else:
                raise RuntimeError("Type error in binary operation")
        elif node.type == tokens.TT_MINUS:
            # Perform subtraction
            return Number(self.visit(node.left_node).value - self.visit(node.right_node).value)
        elif node.type == tokens.TT_MULTIPLY:
            # Perform multiplication
            return Number(self.visit(node.left_node).value * self.visit(node.right_node).value)
        elif node.type == tokens.TT_DIVIDE:
            # Perform division
            return Number(self.visit(node.left_node).value / self.visit(node.right_node).value)
        elif node.type == tokens.TT_MODULO:
            # Perform modulo operation
            return Number(self.visit(node.left_node).value % self.visit(node.right_node).value)
        else:
            raise RuntimeError("Unknown binary operator")

    def visit_unary_node(self, node: UnaryNode):
        # Visit a unary node and perform the appropriate unary operation
        value = self.visit(node.node)
        if node.type == tokens.TT_PLUS:
            if isinstance(value, Number):
                return Number(+value.value)
            else:
                raise RuntimeError("Type error in unary operation")
        elif node.type == tokens.TT_MINUS:
            if isinstance(value, Number):
                return Number(-value.value)
            else:
                raise RuntimeError("Type error in unary operation")
        else:
            raise RuntimeError("Unknown token type for UnaryNode")
