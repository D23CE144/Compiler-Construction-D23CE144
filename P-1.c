#include <stdio.h>
#include <string.h>
int main() 
{
    char input[100];
    int i = 0, valid = 1;
    // Get input from the user
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    // Remove trailing newline character if present
    input[strcspn(input, "\n")] = '\0';
    // Check for zero or more 'a's
    while (input[i] == 'a') 
	{
        i++;
    }
    // Check for "bb" at the end
    if (input[i] == 'b' && input[i + 1] == 'b' && input[i + 2] == '\0') 
	{
        valid = 1; // String is valid
    } 
	else 
	{
        valid = 0; // String is invalid
    }
    // Print result
    if (valid) 
	{
        printf("Valid String\n");
    } 
	else 
	{
        printf("Invalid String\n");
    }
    return 0;
}
