
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
print("Thank you, everyone")

for value in range(1,5):
    print(value)

numbers = list(range(1,5))
print(numbers)

even_numbers = list(range(2,6,2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

s = [value**2 for value in range(1,11)]
print(s)

players = ['charles','martina','michael','forence','eli']
print(players[0:3])
print(players[1:3])
print(players[1:])
print(players[:3])

print(players[-3:])

for player in players[-3:]:
    print(player.title())

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(my_foods)
print(friend_foods)

another_foods = my_foods
another_foods.pop()

print(my_foods)
print(another_foods)
