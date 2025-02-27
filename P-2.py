class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def validate_string(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return "Invalid String"
        return "Valid String" if current_state in self.accept_states else "Invalid String"

# Input reading
num_symbols = int(input("Number of input symbols: "))
alphabet = input("Input symbols: ").split()
states = int(input("Enter number of states: "))
start_state = int(input("Initial state: "))
num_accepting = int(input("Number of accepting states: "))
accept_states = set(map(int, input("Accepting states: ").split()))

# Reading transition table
transitions = {}
num_transitions = int(input("Enter number of transitions: "))
print("Enter transitions in format: current_state input_symbol next_state")
for _ in range(num_transitions):
    state_from, symbol, state_to = input().split()
    transitions[(int(state_from), symbol)] = int(state_to)

# Creating Finite Automaton
fa = FiniteAutomaton(states, alphabet, transitions, start_state, accept_states)

# Input string to validate
input_string = input("Input string: ")

# Output validation result
print(fa.validate_string(input_string))
