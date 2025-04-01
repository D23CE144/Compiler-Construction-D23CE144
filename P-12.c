#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_EXPR 100

// Function prototypes
char* optimizeExpression(const char *expr);
int isOperator(char c);
int isDigitOrVariable(char c);
int evaluateSimpleExpression(int left, char op, int right);

// Function to check if a character is an operator
int isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/');
}

// Function to check if a character is a digit or a variable
int isDigitOrVariable(char c) {
    return (isdigit(c) || isalpha(c));
}

// Function to evaluate simple constant expressions
int evaluateSimpleExpression(int left, char op, int right) {
    switch (op) {
        case '+': return left + right;
        case '-': return left - right;
        case '*': return left * right;
        case '/': return (right != 0) ? left / right : 0;
        default: return 0;
    }
}

// Function to optimize the expression
char* optimizeExpression(const char *expr) {
    static char optimized[MAX_EXPR];
    char temp[MAX_EXPR];
    int i = 0, j = 0, numStack[2] = {0, 0}, numIndex = 0;
    char op = 0;

    while (expr[i] != '\0') {
        if (isdigit(expr[i])) {
            numStack[numIndex] = 0;
            while (isdigit(expr[i])) {
                numStack[numIndex] = numStack[numIndex] * 10 + (expr[i] - '0');
                i++;
            }
            numIndex++;
        } else if (isOperator(expr[i]) && numIndex == 1) {
            op = expr[i];
            i++;
        } else if (isalpha(expr[i]) || expr[i] == '(' || expr[i] == ')') {
            temp[j++] = expr[i++];
        } else {
            i++;
        }

        if (numIndex == 2) {
            int result = evaluateSimpleExpression(numStack[0], op, numStack[1]);
            sprintf(temp + j, "%d", result);
            j += strlen(temp + j);
            numIndex = 0;
        }
    }
    temp[j] = '\0';
    strcpy(optimized, temp);
    return optimized;
}

int main() {
    char input[MAX_EXPR];
    printf("Enter an arithmetic expression: ");
    fgets(input, MAX_EXPR, stdin);
    input[strcspn(input, "\n")] = 0;

    char *optimized = optimizeExpression(input);
    printf("Optimized Expression: %s\n", optimized);

    return 0;
}
