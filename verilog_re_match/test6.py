import re

# Define the input string
input_string = "    mgmtsoc_interrupt = 32'd0;"
#input_string = "reg mgmtsoc_interrupt = 32'd0;"

# Define the regular expression pattern
pattern = r"^\s+(\w+) ="

# Use the re.search() function to find the pattern in the input string
match = re.search(pattern, input_string)

# Check if a match is found
if match:
    # Access the matched values using group() or groups()
    s = match.group(1)

    print(f"s: {s}")
else:
    print("No match found.")




