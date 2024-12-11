#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def get_names(filename):
    with open(filename) as file:
        names_list = file.readlines()
    return names_list

def get_template(filename):
    with open(filename) as file:
        temp = file.read()
    return temp

names = get_names('./Input/Names/invited_names.txt')
template = get_template('./Input/Letters/starting_letter.txt')


for name in names:
    name = name.strip()
    with open(f'./Output/{name}_letter.txt',mode="w") as file:
        letter = template
        letter = letter.replace("[name]",f"{name}")
        file.write(letter)