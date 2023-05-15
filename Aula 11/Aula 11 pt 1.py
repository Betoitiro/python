with open('Moby-Dick.txt', 'r', encoding= 'utf-8') as file_object:
    cont = file_object.read()


with open('Moby-Dick.txt', 'a') as file_object:
    file_object.write("eu amo programar\n")