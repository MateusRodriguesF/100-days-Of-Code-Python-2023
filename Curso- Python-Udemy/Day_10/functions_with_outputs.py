# functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it tor return the title case version of the name"""
        # DocString 👆
    if f_name == "" or l_name == "":
        return "You must provide valid name."
    print(f_name.title())
    print(l_name.title())
    return f_name.title() + " " + l_name.title()

# name = input("Type your name: ")
# surname = input("Type your surname: ")
# print(format_name(name, surname))

print(format_name(input("What is your first name? : "), input("What is your last name? : ")))