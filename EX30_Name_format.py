# def format_name(fname, lname):
#     print(fname.title())
#     print(lname.title())
#
#
# format_name("MAulik", "patel")

#
# def format_name(fname, lname):
#     formated_fname = fname.title()
#     formated_lname = lname.title()
#
#     print(f"{formated_fname} {formated_lname}")
#
# format_name("mack", "patel")


def format_name(fname, lname):
    """It takes first and last name as input
    and gives a return value as a formatted string"""
    if fname == "" or lname == "":
        return "Please enter a valid input."
    formated_fname = fname.title()
    formated_lname = lname.title()

    return f"Result: {formated_fname} {formated_lname}"


# formetd_str = format_name("mack", "patel")
# print(formetd_str)

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
