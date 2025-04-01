from collections import defaultdict

# Grammar definition
grammar = {
    "S": [["A", "B", "C"], ["D"]],
    "A": [["a"], ["ε"]],
    "B": [["b"], ["ε"]],
    "C": [["(", "S", ")"], ["c"]],
    "D": [["A", "C"]]
}

non_terminals = list(grammar.keys())
terminals = {"a", "b", "c", "(", ")", "$"}
first = defaultdict(set)
follow = defaultdict(set)
parsing_table = defaultdict(dict)

# Compute First sets
def compute_first():
    epsilon = "ε"
    def first_of(symbol):
        if symbol in first and first[symbol]:
            return first[symbol]
        if symbol not in non_terminals:
            return {symbol}
        for production in grammar[symbol]:
            contains_epsilon = True
            for s in production:
                s_first = first_of(s)
                first[symbol].update(s_first - {epsilon})
                if epsilon not in s_first:
                    contains_epsilon = False
                    break
            if contains_epsilon:
                first[symbol].add(epsilon)
        return first[symbol]
    for nt in non_terminals:
        first_of(nt)

# Compute Follow sets
def compute_follow():
    follow["S"].add("$")
    def follow_of(nt):
        for lhs, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol == nt:
                        next_symbols = production[i+1:]
                        if next_symbols:
                            first_next = set()
                            for s in next_symbols:
                                first_s = first[s]
                                first_next.update(first_s - {"ε"})
                                if "ε" not in first_s:
                                    break
                            else:
                                first_next.update(follow[lhs])
                            follow[symbol].update(first_next)
                        else:
                            follow[symbol].update(follow[lhs])
    for _ in range(len(non_terminals)):
        for nt in non_terminals:
            follow_of(nt)

# Construct Predictive Parsing Table
def construct_parsing_table():
    for nt in grammar:
        for production in grammar[nt]:
            first_set = set()
            contains_epsilon = True
            for symbol in production:
                first_of_symbol = first[symbol]
                first_set.update(first_of_symbol - {"ε"})
                if "ε" not in first_of_symbol:
                    contains_epsilon = False
                    break
            if contains_epsilon:
                first_set.update(follow[nt])
            for terminal in first_set:
                parsing_table[nt][terminal] = production

# Check if the grammar is LL(1)
def is_LL1():
    for nt in parsing_table:
        seen = set()
        for terminal in parsing_table[nt]:
            if terminal in seen:
                return False
            seen.add(terminal)
    return True

# Validate input string
def validate_string(input_str):
    stack = ["S", "$"]
    input_str += "$"
    index = 0
    while stack:
        top = stack.pop()
        if top == "$" and input_str[index] == "$":
            return "Valid string"
        elif top in terminals:
            if top == input_str[index]:
                index += 1
            else:
                return "Invalid string"
        elif top in non_terminals:
            if input_str[index] in parsing_table[top]:
                stack.extend(reversed(parsing_table[top][input_str[index]]))
            else:
                return "Invalid string"
        else:
            return "Invalid string"
    return "Invalid string"

compute_first()
compute_follow()
construct_parsing_table()

# Print Parsing Table
print("Predictive Parsing Table:")
for nt, rules in parsing_table.items():
    print(f"{nt}: {rules}")

# Check if Grammar is LL(1)
if is_LL1():
    print("The grammar is LL(1)")
else:
    print("The grammar is not LL(1)")

# Test Cases
test_cases = ["abc", "a", "ac", "(abc)", "(ab)", "abcabc", "(ac)", "b"]
for test in test_cases:
    print(f"{test}: {validate_string(test)}")
