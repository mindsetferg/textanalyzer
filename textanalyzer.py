import sys
import re
script, file = sys.argv

the_author = input("Who is the author of the book you are analyzing?")
the_title = input("What is the title of the book you are analyzing?")

text_import = open(file)
full_text = text_import.read()
list_text = full_text.split()

final_list = list()

for item in list_text:
    if item.isalnum() == True:
        final_list.append(item.lower())

    elif item.isalnum() == False:
        text_container = list()
        text_container = re.split("[= : ; , . - ( ) ! | ? ' |\n |\s \W]", item)
        for pieces in text_container:
            if pieces.isalnum() == True and len(pieces) > 1:
                final_list.append(pieces.lower())

print(f"> {the_author}'s '{the_title}' contains {len(full_text)} characters")
print(f"> {the_author}'s '{the_title}' contains {len(final_list)} words")

print("Now let's dive deeper!")
