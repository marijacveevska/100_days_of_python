#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Read the starting letter
with open("Day 24/mail_merge_project/Input/Letters/starting_letter.txt") as letter:
    letter_template = letter.read()

# Read names and create letters
with open("Day 24/mail_merge_project/Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

    for name in name_list:
        clean_name = name.strip()
        personalized_letter = letter_template.replace("[name]", clean_name)

        with open(
            f"Day 24/mail_merge_project/Output/ReadyToSend/{clean_name}.txt",
            mode="w"
        ) as new_letter:
            new_letter.write(personalized_letter)