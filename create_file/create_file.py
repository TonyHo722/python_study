
# create output file
writefile = open("test.txt", "w")
line_number = 100
for num in range(1, 10000):
    print(num)
    writefile.write(f"number = {num}\n")

writefile.close()
