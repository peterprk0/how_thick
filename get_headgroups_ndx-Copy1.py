#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re

def get_z_middle(file_gro):
    with open(file_gro, 'r') as file:
        for line in file:
            pass # Read all lines
        last_line = line.strip().split()
        return float(last_line[2])/2

def get_headgroups_ndx(input_file_gro, lipid, lipid_headgroup, z_middle):
    index_upper = []
    index_lower = []

    def is_numeric_list(lst): # This function checks if all the strings in a list are numbers 
        try:
            return all(isinstance(float(i), float) for i in lst)
        except ValueError:
            return False
    
    with open(input_file_gro, 'r') as file: # read the file
        for line in file: # check line by line
        
            pattern = rf"{lipid}|\s+|{lipid_headgroup}"         # selecting only the lines of the Phosphorus of POPC
            if lipid in line and lipid_headgroup in line:
                split_result = re.split(pattern, line.strip())
                split_result = [s for s in split_result if s]
                if is_numeric_list(split_result):
                    # now sorting the headgroup atom from upper and lower
                    if float(split_result[4]) < z_middle: 
                        index_lower.append(split_result[1])
                    else:
                        index_upper.append(split_result[1])
    
        with open('headgroups.ndx', 'w') as output:
            output.write('[ headgroup_upper ]' + "\n")
            for i in range(0, len(IL_index_upper), 15):  # Process in chunks of 15
                line = " ".join(map(str, IL_index_upper[i:i+15]))  # Convert numbers to strings and join
                output.write(line + "\n")  # Write to file with a newline
                
            output.write("\n")
            output.write('[ headgroup_lower ]' + "\n")
            for i in range(0, len(IL_index_lower), 15):  # Process in chunks of 15
                line = " ".join(map(str, IL_index_lower[i:i+15]))  # Convert numbers to strings and join
                output.write(line + "\n")  # Write to file with a newline

z_middle = get_z_middle('md.gro')
get_headgroups_ndx('md.gro', 'POPC','P', z_middle)

