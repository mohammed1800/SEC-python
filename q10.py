def count_characters(string):
    char_count = {}  # Initialize an empty dictionary to store character counts
    for char in string:
        if char in char_count:
            char_count[char] += 1  # Increment count if character is already in dictionary
        else:
            char_count[char] = 1  # Add character to dictionary with count 1 if not already present
    return char_count

# Input a string from the user
input_string = input("Enter a string: ")

# Call the count_characters function to count characters in the string
char_counts = count_characters(input_string)

# Print the character counts stored in the dictionary
print("Character counts in the string:")
for char, count in char_counts.items():
    print(f"'{char}': {count}")
