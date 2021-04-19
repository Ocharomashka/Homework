from googletrans import Translator

with open('text_4_new.txt', 'w', encoding='utf-8') as file:
    with open('text_4.txt', 'r', encoding= 'utf-8')as init_f:
        trans = init_f.read()
    try:
        file.write(Translator().translate(trans, dest="ru").trans)
    except AttributeError:
        print('Alarm')

