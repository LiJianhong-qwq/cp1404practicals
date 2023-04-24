"""
Expect: 30 min
Actually: 20 min
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

language_list = [python, ruby, visual_basic]
display_list = []
for i in language_list:
    if i.is_dynamic():
        display_list.append(i.name)

print("The dynamically typed languages are:")
for name in display_list:
    print(name)



