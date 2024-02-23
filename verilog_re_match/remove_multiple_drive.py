import re
# Open the file in read mode
file = open("mgmt_core.patrick.v", "r")
#file = open("input.txt", "r")

# Read the entire file content as a single string
Lines = file.readlines()

pattern_reg_only_init = r"reg (\S+) ="
pattern_reg_array_init = r"reg \[(\d+):(\d+)\] (\S+) ="

pattern_reg_only_NBA = r"^\s+(\w+) <="
pattern_reg_onebit_NBA = r"^\s+(\w+)\[(\d+)\] <="
pattern_reg_array_NBA = r"^\s+(\w+)\[(\d+):(\d+)\] <="
pattern_reg_only_BA  = r"^\s+(\w+) ="
pattern_reg_onebit_BA = r"^\s+(\w+)\[(\d+)\] ="
pattern_reg_array_BA = r"^\s+(\w+)\[(\d+):(\d+)\] ="

warning_count = 0
reg_only_init_count = 0
reg_array_init_count = 0
reg_only_dict = {}
reg_array_dict = {}

# match string for  reg with init value
for line in Lines:
    match_reg_only_init = re.search(pattern_reg_only_init, line)
    if match_reg_only_init:
        s = match_reg_only_init.group(1)
        reg_only_dict[s] = 0
        print(f"reg_only_dict s: {s}")
        reg_only_init_count += 1

    match_reg_array_init = re.search(pattern_reg_array_init, line)
    if match_reg_array_init:
        s = match_reg_array_init.group(3)
        reg_array_dict[s] = 0
        print(f"reg_array_dict s: {s}")
        reg_array_init_count += 1


reg_only_NBA_count = 0
reg_array_NBA_count = 0
reg_only_BA_count = 0
reg_array_BA_count = 0

# match string with non-block-assignment(NBA)  and block-assignment(BA)
for line in Lines:
    match_reg_only_NBA = re.search(pattern_reg_only_NBA, line)
    if match_reg_only_NBA:
        s = match_reg_only_NBA.group(1)
        if s in reg_only_dict :
            if reg_only_dict.get(s) == 0 :
                reg_only_dict.update({s:1})
                print(f"reg_only_dict s: {s} = 1, match_reg_only_NBA")
                reg_only_NBA_count += 1
        elif s in reg_array_dict :
            if reg_array_dict.get(s) == 0 :
                reg_array_dict.update({s:1})
                print(f"reg_array_dict s: {s} = 1, match_reg_only_NBA")
                reg_array_NBA_count += 1

    match_reg_onebit_NBA = re.search(pattern_reg_onebit_NBA, line)
    if match_reg_onebit_NBA:
        s = match_reg_onebit_NBA.group(1)
        if s in reg_only_dict :
            warning_count += 1
            print("warning_detect : match_reg_onebit_NBA found in reg_only_dict, it should not happend!!!")
        elif s in reg_array_dict :
            if reg_array_dict.get(s) == 0 :
                reg_array_dict.update({s:1})
                print(f"reg_array_dict s: {s} = 1, match_reg_onebit_NBA")
                reg_array_NBA_count += 1

    match_reg_array_NBA = re.search(pattern_reg_array_NBA, line)
    if match_reg_array_NBA:
        s = match_reg_array_NBA.group(1)
        if s in reg_array_dict :
            if reg_array_dict.get(s) == 0 :
                reg_array_dict.update({s:1})
                print(f"reg_array_dict s: {s} = 1, match_reg_array_NBA")
                reg_array_NBA_count += 1

    match_reg_only_BA = re.search(pattern_reg_only_BA, line)
    #if not match_reg_only_init and not match_reg_array_init:
    if match_reg_only_BA:
        s = match_reg_only_BA.group(1)
        if s in reg_only_dict :
            if reg_only_dict.get(s) == 0 :
                reg_only_dict.update({s:1})
                print(f"reg_only_dict s: {s} = 1, match_reg_only_BA")
                reg_only_BA_count += 1
        elif s in reg_array_dict :
            if reg_array_dict.get(s) == 0 :
                reg_array_dict.update({s:1})
                print(f"reg_array_dict s: {s} = 1, match_reg_only_BA")
                reg_array_BA_count += 1

    match_reg_onebit_BA = re.search(pattern_reg_onebit_BA, line)
    if match_reg_onebit_BA:
        s = match_reg_onebit_BA.group(1)
        if s in reg_only_dict :
            if reg_only_dict.get(s) == 0 :
                reg_only_dict.update({s:1})
                print(f"reg_only_dict s: {s} = 1, match_reg_onebit_BA")
                reg_only_BA_count += 1
        elif s in reg_array_dict :
            if reg_array_dict.get(s) == 0 :
                reg_array_dict.update({s:1})
                print(f"reg_array_dict s: {s} = 1, match_reg_onebit_BA")
                reg_array_BA_count += 1

    match_reg_array_BA = re.search(pattern_reg_array_BA, line)
    if match_reg_array_BA:
        s = match_reg_array_BA.group(1)
        #print(f"match_reg_array_BA s: {s} ")
        if s in reg_only_dict :
            if reg_only_dict.get(s) == 0 :
                reg_only_dict.update({s:1})
                print(f"reg_only_dict s: {s} = 1, match_reg_array_BA")
                reg_only_BA_count += 1
        elif s in reg_array_dict :
            if reg_array_dict.get(s) == 0 :
                reg_array_dict.update({s:1})
                print(f"reg_array_dict s: {s} = 1, match_reg_array_BA")
                reg_array_BA_count += 1

# create output file
writefile = open("output.txt", "w")

for line in Lines:
    match_reg_only_init = re.search(pattern_reg_only_init, line)
    if match_reg_only_init:
        s = match_reg_only_init.group(1)
        if reg_only_dict.get(s) == 1 :
            modify_line = "reg " + s + ";\n"
            #print(modify_line)
            writefile.write(modify_line)
            continue
        elif reg_only_dict.get(s) == 0 :
            modify_line = line.replace('reg', 'wire')
            print(modify_line)
            print("replace to wire only")
            writefile.write(modify_line)
            continue

    match_reg_array_init = re.search(pattern_reg_array_init, line)
    if match_reg_array_init:
        s = match_reg_array_init.group(3)
        x = match_reg_array_init.group(1)
        y = match_reg_array_init.group(2)
        if reg_array_dict.get(s) == 1 :
            modify_line = "reg [" + x + ":" + y + "] " + s + ";\n"
            #print(modify_line)
            #print(f"reg [{x}:{y}] {s};")
            writefile.write(modify_line)
            continue
        elif reg_array_dict.get(s) == 0 :
            modify_line = line.replace('reg', 'wire')
            print("line.replase = ", line.replace('reg', 'wire'))
            print(modify_line)
            print("replace to wire array")
            writefile.write(modify_line)
            continue

    writefile.write(line)

writefile.close()


print(f"warning_count: {warning_count}")
print(f"reg_only_init_count: {reg_only_init_count}")
print(f"reg_array_init_count: {reg_array_init_count}")
print(f"reg_only_NBA_count: {reg_only_NBA_count}")
print(f"reg_array_NBA_count: {reg_array_NBA_count}")
print(f"reg_only_BA_count: {reg_only_BA_count}")
print(f"reg_array_BA_count: {reg_array_BA_count}")

print(f"reg_only_A_count: {reg_only_BA_count+reg_only_NBA_count}")
print(f"reg_array_A_count: {reg_array_BA_count+reg_array_NBA_count}")

print(f"reg_only_dict: {reg_only_dict}")
print(f"reg_array_dict: {reg_array_dict}")
# Close the file
file.close()