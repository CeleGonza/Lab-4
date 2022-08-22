from io import open

def escribir(lineaNueva):
    contText=open("contactos.txt","r+")
    lineaTexto=""
    lineas=contText.readlines()
    contText.seek(0)
    contText.writelines(lineas)
    contText.close()

def imprimir():
    contText=open("contactos.txt","r+")
    lineaTexto=""
    print(contText.read())

    contText.close()

escribir("Louisa 86152112")
imprimir()
