
def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' '+ last_name
    return full_name.title()


while True:
    answer = input("quit enter q: ")
    if answer == 'q':
        break
    else:
        print('\nPlease tell me your name: ')
    
        f_name = input("First name: ")
        m_name = input("Middle name: ")
        l_name = input("Last name: ")


    fullname = formatted_name(f_name, l_name, m_name)
    print("\nHello, " + fullname + "!")


