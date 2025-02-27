from collections import defaultdict

def compute_first(grammar, non_terminals):
    first = defaultdict(set)
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
    return first

def compute_follow(grammar, non_terminals, first):
    follow = defaultdict(set)
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
    
    return follow

if __name__ == "__main__":
    grammar = {
        "S": [["A", "B", "C"], ["D"]],
        "A": [["a"], ["ε"]],
        "B": [["b"], ["ε"]],
        "C": [["(", "S", ")"], ["c"]],
        "D": [["A", "C"]]
    }
    non_terminals = ["S", "A", "B", "C", "D"]
    
    first_sets = compute_first(grammar, non_terminals)
    follow_sets = compute_follow(grammar, non_terminals, first_sets)
    
    print("First sets:")
    for nt in non_terminals:
        print(f"First({nt}) = {{", ", ".join(sorted(first_sets[nt])), "}")
    
    print("\nFollow sets:")
    for nt in non_terminals:
        print(f"Follow({nt}) = {{", ", ".join(sorted(follow_sets[nt])), "}")
