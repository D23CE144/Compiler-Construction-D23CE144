def main():
    # Input the number of input symbols
    num_symbols = int(input("Enter number of input symbols: "))
    
    print("Input symbols: ", end="")
    symbols = input().split()  # Input symbols as space-separated values

    # Input the number of states
    num_states = int(input("Enter number of states: "))

    # Input the initial state
    initial_state = int(input("Initial state: "))

    # Input the number of accepting states
    num_accept_states = int(input("Number of accepting states: "))

    print("Accepting states: ", end="")
    accept_states = list(map(int, input().split()))  # Input accepting states as space-separated values

    # Input the transition table
    print("Transition table (format: from_state input_symbol to_state):")
    transition_table = {}
    num_transitions = num_states * num_symbols  # Total transitions
    for _ in range(num_transitions):
        from_state, input_symbol, to_state = input().split()
        from_state = int(from_state)
        to_state = int(to_state)
        transition_table[(from_state, input_symbol)] = to_state

    # Input the string to validate
    input_string = input("Input string: ")

    # Validate the string
    current_state = initial_state
    for char in input_string:
        if (current_state, char) in transition_table:
            current_state = transition_table[(current_state, char)]
        else:
            print("Invalid String")
            return

    # Check if the final state is an accepting state
    if current_state in accept_states:
        print("Invalid String")
    else:
        print("Valid String")


if __name__ == "__main__":
    main()
