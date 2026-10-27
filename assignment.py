# You can remove 'pass' if you written code in the function
# Exercise 1

def read_line(filename, line_number):
    # Write your code here
    pass

# Exercise 2
def reverse_lines(source, destination):
     f_src = open(source, "r")
    lines = f_src.readlines()
    f_src.close()
    
    f_dst = open(destination, "w")
    count = 0
    for line in reversed(lines):
        clean_line = line.strip()
        f_dst.write(clean_line + "\n")
        count += 1
    f_dst.close()
    
    return count

# Exercise 3
def merge_files(first, second, destination):
    # Write your code here
    pass

# Exercise 4
def find_score(filename, name):
    # Write your code here
    pass

# Exercise 5
def update_score(filename, name, new_score):
    # Write your code here
    pass
