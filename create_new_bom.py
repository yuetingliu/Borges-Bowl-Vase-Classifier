# This script is used to generate new bom files
# method: locate the coordinates (x,y) and change the values

import os
import numpy as np

def load_bom_file(bom_file):
    # Store all lines in a list
    with open(bom_file, 'r') as f:
        bom = f.readlines()
    return bom

# Find lines that contain editable values x:, y:
def find_line(bom):
    lines = []
    for num, line in enumerate(bom):
        if '"x":' in line or '"y":' in line:
            lines.append(num)
    return lines
 
 # Find the numerical values in a line 
def find_numericals(line):
    nums = []
    for num, char in enumerate(line):
        try:
            float(char)
            nums.append(num)
        except ValueError:
            pass
    return nums

# Main function
def create_new_bom(bom_file, seed=0, save_path='./new_image_files'):
    # Load bom file 
    bom = load_bom_file(bom_file)
    # Find line nums that contain changeable numerical values
    line_nums = find_line(bom)
    # Iterate through all lines
    
    for line_num in line_nums:
        line= bom[line_num]
        nums = find_numericals(line)
        # Get the string value of the line
        start, end = nums[0], nums[-1]
        str_value = line[start:end]
        # Modify the string value by multiplying a value ranging (0.7, 1.4)
        np.random.seed(seed)
        multiplier = np.random.choice(np.arange(0.7, 1.4, 0.02))
        modified = str(float(str_value)*multiplier)
        # Replace the original string
        bom[line_num] = line.replace(str_value, modified)
    # Save the new bom file 
    path = save_path
    if not os.path.exists(path):
        os.mkdir(path)
    name = ''.join(['new',str(seed),'_', bom_file.split('/')[-1]])
    with open(os.path.join(path, name), 'w') as f:
        f.write(''.join(bom))    
    return bom