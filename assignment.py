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
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
