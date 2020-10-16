# the Zen of python
zen_of_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one—and preferably only one—obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea—let's do more of those!'''
#print(zen_of_python + '\n')

# count of 'better', 'never', 'is'
zen_find_better = zen_of_python.find('better')
zen_find_never = zen_of_python.find('never')
zen_find_is = zen_of_python.find('is')
print('better =', + zen_find_better, 'never =', + zen_find_never, 'is =', + zen_find_is + '\n')

# upper case
zen_upper_case = zen_of_python.upper()
print(zen_upper_case + '\n')

# replace 
zen_lower_case = zen_of_python.lower()
zen_of_python_without_i = zen_lower_case.replace('i', '&')
print(zen_of_python_without_i + '\n')
