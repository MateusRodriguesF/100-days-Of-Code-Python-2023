PLACEHOLDER = "[name]"


with open(r"Day_24\Mail Merge Project\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

with open(r"Day_24\Mail Merge Project\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip() # Remove the \n generated from each line of list names
        new_letter = letter_contents.replace(PLACEHOLDER, name)

        with open(rf"Day_24\Mail Merge Project\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)