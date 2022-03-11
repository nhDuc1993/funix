#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import re
from statistics import mean, median

import pandas as pd
import numpy as np

d = os.getcwd() + '\Data Files\\'


# ## Task 1

# In[ ]:


print('-'*15 + 'Task1' + '-'*15 + '\n')

while True:
    try:
        file_name = input('Enter file names: ')
        file_dir = d + file_name + '.txt'
        
        if file_name == 'close': #type "close" to close the program
            break
        else:
            with open(file_dir, 'r') as f:
                print(f.read())

            print('\n' + file_name + ' opened successfully')
            break

    except:
        print('File not found! Please enter the file name again.\n' )
        continue


# ## Task 2

# In[ ]:


print('\n' + '-'*15 + 'Task2' + '-'*15 )

with open(file_dir, 'r') as f:
    lines = f.readlines()


# In[ ]:


print('\n' + '*' *5, 'REPORT', '*' *5)

valid_lines = 0
invalid_lines = 0

invalid_con1 = []
invalid_con2 = []

for i, l in enumerate(lines):
    lst = l.split(',')
    
    con1 = (len(lst)==26) # 26 values separated by a comma
    
    pattern = re.compile("^N[0-9]{8}$")
    s = lst[0]
    con2 = bool(re.match(pattern, s)) # Student ID matches the pattern
    
    if con1 and con2:
        valid_lines +=1
    else:
        invalid_lines += 1
        
    if not con1:
        invalid_con1.append(i)
    
    if not con2:
        invalid_con2.append(i)

        
print('- Valid lines: ', valid_lines)
print('- Invalid lines: ', invalid_lines)
if invalid_lines > 0: # Will list out the incorrect lines if there is any
    print('\n' + '*' *5, 'LIST OF INVALID LINES', '*' *5)
    print('- Does not contain 26 values: ')
    for i in invalid_con1:
        print(lines[i])

    print('- Wrong student ID format: ')
    for i in invalid_con2:
        print(lines[i])


# ## Task 3

# In[ ]:


print('\n' + '-'*15 + 'Task3' + '-'*15 )


# In[ ]:


print('\n' + '*' *5, 'ANALYSIS', '*' *5)
print('// Only applies to valid lines')

invalid_lines_index = set(invalid_con1 + invalid_con2)
valid_lines_list = [l for i,l in enumerate(lines) if i not in invalid_lines_index ]


# In[ ]:


answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')

grade_list = []

for line in valid_lines_list:
    grade = 0
    
    answer = line.split(',')[1:26]
    answer[-1] = answer[-1].replace('\n', '') # remove \n
    
    for i,j in zip(answer, answer_key):
        if i == '':
            grade += 0
        elif i == j:
            grade += 4
        else:
            grade +=-1
    
    grade_list.append(grade)

print('- Average grade: ', mean(grade_list))
print('- Highest grade: ', max(grade_list))
print('- Lowest grade: ', min(grade_list))
print('- Range of grades: ', max(grade_list) - min(grade_list))
print('- Median grade: ', median(grade_list))


# ## Task 4

# In[ ]:


print('\n' + '-'*15 + 'Task4' + '-'*15 )
print('Exporting File')


# In[ ]:


answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')

grade_list = []

for line in valid_lines_list:
    grade = 0
    
    id = line.split(',')[0]
    answer = line.split(',')[1:26]
    answer[-1] = answer[-1].replace('\n', '') # remove \n
    
    for i,j in zip(answer, answer_key):
        if i == '':
            grade += 0
        elif i == j:
            grade +=4
        else:
            grade +=-1
    
    grade_list.append(id + ',' + str(grade))


# In[ ]:


output = os.getcwd() + '\Data Files\\Expected Output\\' + file_name + '_grades.txt'
os.getcwd() + '\Data Files\\'

with open(output, 'w') as o:
    for line in grade_list:
        o.write(line)
        o.write('\n')

