
filename = 'alice'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry the file "+filename+" does not exist.")
else:
    words = contents.split()
    num_words = len(words)
    print("number words "+num_words)
