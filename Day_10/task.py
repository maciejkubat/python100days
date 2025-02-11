def format_name(f_name, l_name):
    """Take a first and last name and format it into title case and return it"""
    f_name = f_name.title()
    l_name = l_name.title()
    full_name = f"{f_name} {l_name}"
    return full_name

full_name = format_name("RoMan", "GierTyCH")
print(full_name)