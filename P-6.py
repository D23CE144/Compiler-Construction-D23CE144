class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input = input_string.replace(" ", "")  # Remove spaces
        self.index = 0

    def parse_S(self):
        if self.index < len(self.input) and self.input[self.index] == 'a':
            self.index += 1
            return True
        elif self.index < len(self.input) and self.input[self.index] == '(':
            self.index += 1  # Consume '('
            if self.parse_L():
                if self.index < len(self.input) and self.input[self.index] == ')':
                    self.index += 1  # Consume ')'
                    return True
            return False
        return False

    def parse_L(self):
        if self.parse_S():
            return self.parse_L_prime()
        return False

    def parse_L_prime(self):
        if self.index < len(self.input) and self.input[self.index] == ',':
            self.index += 1  # Consume ','
            if self.parse_S():
                return self.parse_L_prime()
            return False
        return True  # ε-production

    def validate(self):
        return self.parse_S() and self.index == len(self.input)


# Test cases from the image
test_cases = ["a", "(a)", "(a,a)", "(a,(a,a),a)", "(a,a),(a,a)", "a)", "(a", "a,a", "a,", "(a,a),a"]

# Running test cases
for test in test_cases:
    parser = RecursiveDescentParser(test)
    result = "Valid string" if parser.validate() else "Invalid string"
    print(f"Input: {test} -> {result}")
