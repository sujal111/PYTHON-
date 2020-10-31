email = input("What is your mail address?: ").strip()

user_name = email[:email.index("0")]


domain_name = email[email.index("0")+1:]


output = "Your username is: '{}' and your domain name is '{}'".format(user_name.domain_name)


print(output)