#include <stdio.h>
#include <string.h>
int main() 
{
    char input[100];
    char choice;
    int i, valid;
    do 
	{
        printf("\nDo you want to enter a string? (y/n): ");
        scanf(" %c", &choice); // Read user choice
        switch (choice) 
		{
            case 'y': // User wants to input a string
            case 'Y':
                // Clear input buffer
                while (getchar() != '\n'); 
                printf("Enter a string: ");
                fgets(input, sizeof(input), stdin);
                // Remove trailing newline character if present
                input[strcspn(input, "\n")] = '\0';
                // Reset variables
                i = 0;
                valid = 1;
                // Check for zero or more 'a's
                while (input[i] == 'a') 
				{
                    i++;
                }
                // Check for "bb" at the end
                if (input[i] == 'b' && input[i + 1] == 'b' && input[i + 2] == '\0') {
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
                break;
            case 'n': // User wants to stop
            case 'N':
                printf("Exiting program...\n");
                break;
            default: // Invalid choice
                printf("Invalid choice! Please enter 'y' or 'n'.\n");
                break;
        }
    } 
	while (choice != 'n' && choice != 'N'); // Repeat until user chooses 'n'
    return 0;
}
