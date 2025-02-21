class RecursiveDescentParser:
    def __init__(self, input_string):
        self.str = input_string.replace(" ", "")  # Remove spaces
        self.ip = 0  # Position counter
        self.f = 0  # Error flag

    def S(self):
        """S → ( L ) | a"""
        if self.ip < len(self.str) and self.str[self.ip] == '(':
            self.ip += 1
            self.L()
            if self.ip < len(self.str) and self.str[self.ip] == ')':
                self.ip += 1
            else:
                self.f = 1  # Error: ')' expected
        elif self.ip < len(self.str) and self.str[self.ip] == 'a':
            self.ip += 1
        else:
            self.f = 1  # Error: Neither '(' nor 'a' found

    def L(self):
        """L → S L'"""
        self.S()
        self.L2()

    def L2(self):
        """L' → , S L' | ε"""
        if self.ip < len(self.str) and self.str[self.ip] == ',':
            self.ip += 1
            self.S()
            self.L2()
        # ε case: Do nothing

    def validate(self):
        """Start parsing and check if input is valid"""
        self.S()  # Start from S
        return self.f == 0 and self.ip == len(self.str)


# Taking input from user
user_input = input("Enter a string to validate: ").strip()

# Validate input
parser = RecursiveDescentParser(user_input)
result = "Valid string" if parser.validate() else "Invalid string"
print(f"Input: {user_input} -> {result}")
