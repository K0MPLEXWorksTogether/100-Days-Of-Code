#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def write_letter_to_output(name):
    with open("Input/Letters/starting_letter.txt", "r") as LetterFile:
        content_lines = LetterFile.readlines()
        content_lines[0] = content_lines[0].strip().replace("[name],", f"{name},")
        content_lines[0] += "\n"

        with open(f"Output/ReadyToSend/letter_to_{name}.txt", "w") as WriteFile:
            for content in content_lines:
                WriteFile.write(content)

with open("Input/Names/invited_names.txt", "r") as NamesFile:
    names = NamesFile.readlines()
    for name in names:
        stripped = name.strip()
        write_letter_to_output(stripped)
