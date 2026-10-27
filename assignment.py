# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    if line_number <= 0:
        return ""
    f = open(filename, "r")
    line = ""
    for _ in range(line_number):
        line = f.readline()
        if line == "":
            break
    f.close()
    if line == "":
        return ""
    return line.rstrip("\r\n")

# Exercise 2
def reverse_lines(source, destination):
     fsrc = open(source, "r")
    lines = fsrc.readlines()
    fsrc.close()
    fdst = open(destination, "w")
    count = 0
    for line in reversed(lines):
        clean_line = line.strip()
        fdst.write(clean_line + "\n")
        count += 1
    fdst.close()
    return count

# Exercise 3
def merge_files(first, second, destination):
    f1 = open(first, "r")
    lines1 = f1.readlines()
    f1.close()
    f2 = open(second, "r")
    lines2 = f2.readlines()
    f2.close()
    dest = open(destination, "w")
    count = 0
    for line in lines1:
        dest.write(line.strip() + "\n")
        count += 1
    for line in lines2:
        dest.write(line.strip() + "\n")
        count += 1
    dest.close()
    
    return count

# Exercise 4
def find_score(filename, name):
    f = open(filename, "r")
    score = -1
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[0] == name:
            score = int(parts[1])
            break
    f.close()
    return score
# Exercise 5
def update_score(filename, name, new_score):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    found = False
    new_lines = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[0] == name:
            new_lines.append(f"{name},{new_score}\n")
            found = True
        else:
            if not line.endswith("\n"):
                new_lines.append(line + "\n")
            else:
                new_lines.append(line)
    if found == True:
        f = open(filename, "w")
        for line in new_lines:
            f.write(line)
        f.close()
    return found
