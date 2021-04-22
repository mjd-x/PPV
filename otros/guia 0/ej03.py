def dicci():
    diccionario = dict()
    for i in range(ord('a'), ord('z')+1):
        diccionario[chr(i)] = i
    return diccionario


print(dicci())
