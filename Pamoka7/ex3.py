# Create a function that validates an email address based on user input. 
# Ensure the email address contains exactly one "@" symbol and at least one "." in the domain part, along with other structural validations.

# Example input/output:
# Enter an email address: example@gmail.com
# The email address is valid.

def available_email(email):
    if email.count ("@") != 1:
        return False
    parts = email.split("@")
    username = [0]
    domain = [1]
    if not username:
        return False
    if domain.count (".") !=  1:
        return False
    return True
email_input = input(f"Ender an email address: ")

if available_email(email_input):
    print("El. pašto adresas yra galiojantis.")
else:
    print("El. pašto adresas negaliojantis.")