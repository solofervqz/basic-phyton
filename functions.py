def hello_word():
    print("Hello, Word!")

def hello_word_name(first_name):
    print(f"Hello, {first_name}")

def hello_word_args(*args):
    first_name = args[0]
    second_name = args[1]
    thrid_name = args[2]

    print(args)
    print(type(args)) #Para saber que tipo de variable es
    print(first_name)
    print(f"Hello, {first_name} / {second_name} / {thrid_name} !")

def hello_word_keyword_args(first_person, second_person):
    print(f"Hello, {first_person} / {second_person}")

def hello_world_arbitrary_keywords_args(**kwargs): #Aqui podemos acceder a los argumentos
    print(kwargs)
    print(kwargs.get('second_person')) #se evalua si existe la llave
    print(kwargs.get('first_person')) #se evalua si existe la llave


    if kwargs.get('second_person') is None:
        print('No hay segunda persona')
    else:
        print(f"Hello, {kwargs['first_person']} / {kwargs['second_person']}")
    


#hello_word()
#hello_word_name("Fernanda")
#hello_word_name("José")
#hello_word_args("Fernanda", "Isabel", "Vázquez", "Muñoz")

# hello_word_keyword_args(first_person="Fernanda", second_person="José")
hello_world_arbitrary_keywords_args(first_person="Fernanda" , second_person="José")