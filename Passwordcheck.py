# ask user to enter password
password = input("Enter the password:")

# as long as the password entered is not equal to the actual value
# keep asking user to enter password
while password != 'password123':
    password = input("Enter the password:")

# if user enters right password print below msg
print("Password is correct")

