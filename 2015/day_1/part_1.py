# This function will read from a text file and retrun the text as a variable. 
def read_file(file):
    with open(file) as raw_text:
        text = raw_text.read()
        
    return text

position = 0 
 
number = 0

            
my_input = read_file('text.txt')

for char in my_input:
    
    position += 1
    
    if char == "(":
        number += 1
        
    
    elif char == ")":
        number -= 1
    
    else:
        print("Error")
        
    if number < 0:
     break

print(position)