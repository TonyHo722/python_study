import re

# Define the input string
input_string = "mgmtsoc_interrupt[0] <= mgmtsoc_irq"

# Define the regular expression pattern
pattern = r"(\w+)\[(\d+)\] <="

# Use the re.search() function to find the pattern in the input string
match = re.search(pattern, input_string)

# Check if a match is found
if match:
    # Access the matched values using group() or groups()
    s = match.group(1)

    print(f"s: {s}")
else:
    print("No match found.")




