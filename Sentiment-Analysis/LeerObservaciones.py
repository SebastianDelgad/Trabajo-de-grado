import fitz    #Libreria PyMuPDF

#Transforma un archivo PDF a TXT sin perder la estructura del PDF
def leer_PDF():
    pdf_documento = 'PDF/2017- ll.pdf'
    documento = fitz.open(pdf_documento)
    pdf_a_texto = 'PDF/pdf_a_texto.txt'
    salida = open(pdf_a_texto,"wb")

    for pagina in documento:
        texto =pagina.getText().encode("utf8")
        salida.write(texto)
        salida.write(b"\n----\n")
    salida.close()
    return pdf_a_texto


#Extrae información del archivo TXT desde donde comienzan observaciones a los docentes

#def leerTxt(documento):
def leer_txt():
    tObservaciones = []
    quitarEspacios = []
    with open('PDF/pruebas.txt', "r", encoding='utf8') as archivo:
        for word in archivo:
            if word.strip() == 'Observaciones':
                while (True):
                    linea = archivo.readline()
                    tObservaciones.append(linea.strip())
                    #print(linea)
                    if not linea:
                        break
        archivo.close()

    for word3 in tObservaciones:
        if len(word3) > 0:
            quitarEspacios.append(word3)

    return quitarEspacios
    #print(tObservaciones)

# Almacena los nombres, curso y grupo del curso que enseña el docente

def almacenar_nombres(datos):
    vectorNombres = []

    for nombre in datos:
        if len(nombre) > 18:
            grupo = nombre[len(nombre) - 4] + "" + nombre[len(nombre) - 3] + ""+ nombre[len(nombre) - 2] + "" + nombre[len(nombre) - 1]
            if grupo == "M 50":
                vectorNombres.append(nombre)
            else:
                if grupo == "M 51":
                    vectorNombres.append(nombre)
                else:
                    if grupo == "M 52":
                        vectorNombres.append(nombre)
                    else:
                         if grupo == "M 53":
                            vectorNombres.append(nombre)
                         else:
                             if grupo == "M 54":
                                vectorNombres.append(nombre)
                             else:
                                 if grupo == "M 55":
                                    vectorNombres.append(nombre)
    #print(vectorNombres)
    return vectorNombres


# Texto perfectamente acomodado, se extrajeron saltos de linea innecesarios que se generaban por el formato del PDF

def procesado_txt(datos, vectorNombres):
    vectorFinal = []
    vectorDatosProcesados = []
    nObservación = 0
    union = ""

    for word2 in datos:
        if word2[0].isnumeric():
            if int(word2[0]) > nObservación:
                vectorFinal.append(union)
                union = ""
                nObservación += 1
            else:
                if int(word2[0]) <= nObservación:
                    vectorFinal.append(union)
                    union = ""

        for nombre in vectorNombres:
            if word2 == nombre:
                if len(union) > 0:
                    vectorFinal.append(union)
                    union = ""
                vectorFinal.append(word2)
                break
        else:
            union += word2 + " "

    vectorFinal.append(union)

    #se elimina los elementos vacios que hay en el vector
    for word3 in vectorFinal:
        if len(word3) > 0:
            vectorDatosProcesados.append(word3)


    return vectorDatosProcesados
    #print(vectorDatosProcesada)

def observaciones():

    #pdf = leer_PDF()
    txt = leer_txt()
    nombres = almacenar_nombres(txt)
    procesado = procesado_txt(txt,nombres)
    #print(procesado)
    return procesado


#leerPDF()
observaciones()