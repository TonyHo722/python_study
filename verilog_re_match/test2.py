import re

# Define the input string
input_string = "mgmtsoc_reset_storage[1:0] <= csrbank0_reset0_r;"

# Define the regular expression pattern
pattern = r"(\w+)\[(\d+):(\d+)\] <="


# Use the re.search() function to find the pattern in the input string
match = re.search(pattern, input_string)

# Check if a match is found
if match:
    # Access the matched values using group() or groups()
    x = match.group(2)
    y = match.group(3)
    s = match.group(1)

    #print(f"s: {s}")
    print(f"x: {x}, y: {y}, s: {s}")
else:
    print("No match found.")




