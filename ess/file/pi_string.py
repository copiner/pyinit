
filename = 'pi_digits'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("YES")
else:
    print("NO")

print(pi_string)
print(len(pi_string))



