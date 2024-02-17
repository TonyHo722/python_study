import re

# Define the input string
input_string = "reg [1:0] mgmtsoc_reset_storage = 2'd0;"

# Define the regular expression pattern
pattern = r"reg \[(\d+):(\d+)\] (\S+) ="

# Use the re.search() function to find the pattern in the input string
match = re.search(pattern, input_string)

# Check if a match is found
if match:
    # Access the matched values using group() or groups()
    x = match.group(1)
    y = match.group(2)
    s = match.group(3)

    print(f"x: {x}, y: {y}, s: {s}")
else:
    print("No match found.")



