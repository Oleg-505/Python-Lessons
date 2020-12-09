
# Lesson_06_task_01
text_base = 'Hello Oleg! How are you today, Oleg? Today: employes in "Beetroot", \n are feeling good!'
print(text_base, end='\n\n')

import re    #searching and excluding symbols in the text; Regular Expressions
text_01 = re.split(r' |\?|\!|\,|\"|\n|\:', text_base.lower())
print(text_01, end='\n\n')

text_02 = [] #excluding spaces and building the new list
[text_02.append(item) for item in text_01 if item != '']
print (text_02,end='\n\n')

#excluding spaces and building the new list
my_dict = {i:text_02.count(i) for i in text_02}

print(my_dict)

