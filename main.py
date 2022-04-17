#Get user email adress
print("What is your E-Mail adress? ")
email = input()
#slice out user name
user = email[:email.find("@")]
#slice domain name
domain = email[email.find("@") + 1:]
#format message
output = f"Your username is {user} and your domainname is {domain}."
#display output message
print(output)