
# BOTS

# TERNARY OPERATOR

lang = input('For azeri type az, for english type en, for russian type ru: ')

if lang == 'az':
    print("Salam")
elif lang == 'en':
    print("Hello")
elif lang == 'ru':
    print("Привет")
else:
    print("Please enter correct language: en, az or ru")

problem = input('What is your problem: 1 - price, 2 - no server access: ')

if problem == '1':
    if lang == 'az':
        print("Borc al")
    elif lang == 'en':
        print("Borrow some")
    elif lang == 'ru':
        print("Возьми в долг")
elif problem == '2':
    if lang == 'az':
        print("Kompüteri söndür/yandır")
    elif lang == 'en':
        print("Turn off/on")
    elif lang == 'ru':
        print("Выключить/включить")


