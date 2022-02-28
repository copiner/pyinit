
alien_0 = { 'color':'green','points':5 }
new_points = alien_0['points']
print("Earned "+str(new_points)+" points")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)

alien_1 = {'x_position':0,'y_position':25,'speed':'medium','points':5}
print("Original x-position: "+ str(alien_1['x_position']))

alien_1['speed'] = 'fast'


if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_1['x_position'] = alien_1['x_position'] + x_increment


print("New x-position: " + str(alien_1['x_position']))

del alien_1['points']
print(alien_1)

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
#print(user_0.items())
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value:" + value)

for key in user_0.keys():
    print("\n" + key)

for key in sorted(user_0.keys()):
    print("\n" + key)

if 'username' in user_0.keys():
    print("\n" + user_0['username'])

for val in user_0.values():
    print("\n" + val)

for val in set(user_0.values()):
    print("\n" + val)


aliens = [alien_0, alien_1]

for alien in aliens:
    print(alien)

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the follow toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())




