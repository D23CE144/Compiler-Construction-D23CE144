#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_EXPR 100
#define MAX_QUADS 100

typedef struct {
    char op[3];
    char arg1[10];
    char arg2[10];
    char result[10];
} Quadruple;

Quadruple quads[MAX_QUADS];
int quadIndex = 0, tempVarCount = 0;

void addQuadruple(const char *op, const char *arg1, const char *arg2, const char *result) {
    strcpy(quads[quadIndex].op, op);
    strcpy(quads[quadIndex].arg1, arg1);
    strcpy(quads[quadIndex].arg2, arg2);
    strcpy(quads[quadIndex].result, result);
    quadIndex++;
}

char* newTempVar() {
    static char tempVar[10];
    sprintf(tempVar, "t%d", tempVarCount++);
    return strdup(tempVar);
}

const char* parseExpression(const char **expr);
const char* parseTerm(const char **expr);
const char* parseFactor(const char **expr);

void skipWhitespace(const char **expr) {
    while (**expr == ' ') (*expr)++;
}

const char* parseNumber(const char **expr) {
    static char buffer[10];
    int i = 0;
    while (isdigit(**expr)) {
        buffer[i++] = **expr;
        (*expr)++;
    }
    buffer[i] = '\0';
    return strdup(buffer);
}

const char* parseFactor(const char **expr) {
    skipWhitespace(expr);
    if (**expr == '(') {
        (*expr)++;
        const char* value = parseExpression(expr);
        if (**expr == ')') {
            (*expr)++;
        } else {
            printf("Invalid expression\n");
            exit(1);
        }
        return value;
    } else if (isdigit(**expr)) {
        return parseNumber(expr);
    }
    printf("Invalid expression\n");
    exit(1);
}

const char* parseTerm(const char **expr) {
    const char* left = parseFactor(expr);
    while (**expr == '*' || **expr == '/') {
        char op = **expr;
        (*expr)++;
        const char* right = parseFactor(expr);
        char* temp = newTempVar();
        char opStr[2] = {op, '\0'};
        addQuadruple(opStr, left, right, temp);
        left = temp;
    }
    return left;
}

const char* parseExpression(const char **expr) {
    const char* left = parseTerm(expr);
    while (**expr == '+' || **expr == '-') {
        char op = **expr;
        (*expr)++;
        const char* right = parseTerm(expr);
        char* temp = newTempVar();
        char opStr[2] = {op, '\0'};
        addQuadruple(opStr, left, right, temp);
        left = temp;
    }
    return left;
}

int main() {
    char input[MAX_EXPR];
    printf("Enter an arithmetic expression: ");
    fgets(input, MAX_EXPR, stdin);
    input[strcspn(input, "\n")] = 0;

    const char *expr = input;
    parseExpression(&expr);

    printf("\nQuadruple Table:\n");
    printf("%-10s %-10s %-10s %-10s\n", "Operator", "Operand1", "Operand2", "Result");
    for (int i = 0; i < quadIndex; i++) 
	{
        printf("%-10s %-10s %-10s %-10s\n", quads[i].op, quads[i].arg1, quads[i].arg2, quads[i].result);
    }
    return 0;
}
