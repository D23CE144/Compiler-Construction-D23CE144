import string

MAX_LENGTH = 100

def is_delimiter(chr):
    return chr in {' ', '+', '-', '*', '/', ',', ';', '%', '>', '<', '=', 
                   '(', ')', '[', ']', '{', '}'}

def is_operator(chr):
    return chr in {'+', '-', '*', '/', '<', '='}

def is_identifier(s):
    return s and not s[0].isdigit() and not is_delimiter(s[0])

def is_keyword(s):
    keywords = {"auto", "break", "case", "char", "const", "continue", "default", "do",
                "double", "else", "enum", "extern", "float", "for", "goto", "if",
                "int", "long", "register", "return", "short", "signed", "sizeof", "static",
                "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"}
    return s in keywords

def is_integer(s):
    return s.isdigit()

def get_substring(s, start, end):
    return s[start:end+1]

def lexical_analyzer(input_str):
    left = 0
    right = 0
    length = len(input_str)
    
    while right <= length and left <= right:
        if right < length and not is_delimiter(input_str[right]):
            right += 1
        if right < length and is_delimiter(input_str[right]) and left == right:
            if is_operator(input_str[right]):
                print(f"Token: Operator, Value: {input_str[right]}")
            right += 1
            left = right
        elif (right < length and is_delimiter(input_str[right]) and left != right) or (right == length and left != right):
            sub_str = get_substring(input_str, left, right - 1)
            
            if is_keyword(sub_str):
                print(f"Token: Keyword, Value: {sub_str}")
            elif is_integer(sub_str):
                print(f"Token: Integer, Value: {sub_str}")
            elif is_identifier(sub_str) and not is_delimiter(input_str[right - 1]):
                print(f"Token: Identifier, Value: {sub_str}")
            else:
                print(f"Token: Unidentified, Value: {sub_str}")
            
            left = right

if __name__ == "__main__":
    lex_input = input("Enter Code: ")[:MAX_LENGTH]
    print(f'For Expression "{lex_input}":')
    lexical_analyzer(lex_input)
    print()
