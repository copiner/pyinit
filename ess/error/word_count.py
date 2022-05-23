
filename = 'count'

def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        return len(words)

print(count_words(filename))
