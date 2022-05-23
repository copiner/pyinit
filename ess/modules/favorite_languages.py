
from collections import OrderedDict

favorite_languages = OrderedDict() #ordered dict
#favorite_languages = {}
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'javascript'
favorite_languages['ohil'] = 'c++'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
