#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

int main() {
    char input_string[100];
    int choice,i;
    char continue_choice;

    do {
        // Menu to select the test case
        printf("Choose a test case to validate:\n");
        printf("1. String over 0 and 1 where every 0 is immediately followed by 11\n");
        printf("2. String over a, b, c that starts and ends with the same letter\n");
        printf("3. String over lower-case alphabet and digits, starts with an alphabet only\n");
        printf("Enter your choice (1/2/3): ");
        scanf("%d", &choice);

        // Input the string to validate
        printf("Enter the string to validate: ");
        scanf("%s", input_string);

        // Validation logic for all cases
        bool is_valid = false;
        int len = strlen(input_string);

        switch (choice) {
            case 1: {
                // Validate: String over 0 and 1 where every 0 is immediately followed by 11
                int i = 0;
                is_valid = true;
                while (input_string[i] != '\0') {
                    if (input_string[i] == '0') {
                        // Check if '0' is immediately followed by '11'
                        if (input_string[i + 1] == '1' && input_string[i + 2] == '1') {
                            i += 3; // Skip over "011"
                        } else {
                            is_valid = false;
                            break;
                        }
                    } else if (input_string[i] == '1') {
                        i++; // Move to the next character
                    } else {
                        is_valid = false; // Invalid character
                        break;
                    }
                }
                break;
            }
            case 2: {
                // Validate: String over a, b, c that starts and ends with the same letter
                if (len > 0 && (input_string[0] == 'a' || input_string[0] == 'b' || input_string[0] == 'c') &&
                    (input_string[len - 1] == 'a' || input_string[len - 1] == 'b' || input_string[len - 1] == 'c') &&
                    input_string[0] == input_string[len - 1]) {
                    is_valid = true;
                }
                break;
            }
            case 3: {
                // Validate: String over lower-case alphabet and digits, starts with an alphabet only
                if (isalpha(input_string[0]) && islower(input_string[0])) {
                    is_valid = true;
                    for (i = 1; input_string[i] != '\0'; i++) {
                        if (!isalnum(input_string[i])) {
                            is_valid = false; // Invalid character
                            break;
                        }
                    }
                }
                break;
            }
            default:
                printf("Invalid choice!\n");
                return 1;
        }

        // Output the result
        if (is_valid) {
            printf("Valid String\n");
        } else {
            printf("Invalid String\n");
        }

        // Ask user if they want to continue
        printf("\nDo you want to continue? (yes/no): ");
        scanf("%s", input_string); // Reuse `input_string` to hold the answer
        continue_choice = tolower(input_string[0]);
    } while (continue_choice == 'y');

    printf("Program terminated. Goodbye!\n");
    return 0;
}

