import fitz  # Libreria PyMuPDF
import os


# Transforma un archivo PDF a TXT sin perder la estructura del PDF


def leer_PDF():
    pdf_documento = 'PDF/2017- ll.pdf'
    documento = fitz.open(pdf_documento)
    pdf_a_texto = 'PDF/pdf_a_texto.txt'
    salida = open(pdf_a_texto, "wb")

    for pagina in documento:
        texto = pagina.getText().encode("utf8")
        salida.write(texto)
        salida.write(b"\n----\n")
    salida.close()
    return pdf_a_texto


# Extrae información del archivo TXT desde donde comienzan observaciones a los docentes

#def leer_txt(documento):
def leer_txt():
    tObservaciones = []
    quitarEspacios = []
    module_dir = os.path.dirname(__file__)
    file = os.path.join(module_dir,'pruebas.txt')
    archivo = open(file, mode='r', encoding='utf8')
    for word in archivo:
            if word.strip() == 'Observaciones':
                while (True):
                    linea = archivo.readline()
                    tObservaciones.append(linea.strip())
                    # print(linea)
                    if not linea:
                        break
    

    for word3 in tObservaciones:
        if len(word3) > 0:
            quitarEspacios.append(word3)

    return quitarEspacios
    # print(tObservaciones)

# Almacena los nombres, curso y grupo del curso que enseña el docente


def almacenar_nombres(datos):
    vectorNombres = []

    grupos = ["M 50", "M 51", "M 52", "M 53", "M 54", "M 55"]

    for nombre in datos:
        if len(nombre) > 18:
            grupoPDF = nombre[len(nombre) - 4] + "" + nombre[len(nombre) - 3] + \
                "" + nombre[len(nombre) - 2] + "" + nombre[len(nombre) - 1]
            for grupo in grupos:
                if grupoPDF == grupo:
                    vectorNombres.append(nombre)

    # print(vectorNombres)
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

    # se elimina los elementos vacios que hay en el vector
    for word3 in vectorFinal:
        if len(word3) > 0:
            vectorDatosProcesados.append(word3)

    return vectorDatosProcesados
    # print(vectorDatosProcesada)


def tiempo_calificacion(datosProcesados):

    tamaño = len(datosProcesados) - 1
    dato = datosProcesados[tamaño]
    tamaño = "" + dato
    cantidadObservaciones = [int(temp)
                             for temp in tamaño.split() if temp.isdigit()]
    tiempo = ((cantidadObservaciones[0]) * 1.3) / 60
    tiempoFInal = "Tiempo estimado de procesamiento: " + \
        str((float("{0:.1f}".format(tiempo)))) + " Minutos"

    return tiempoFInal


def observaciones():

    #pdf = leer_PDF()
    txt = leer_txt()
    nombres = almacenar_nombres(txt)
    procesado = procesado_txt(txt, nombres)
    #print(procesado)

    return procesado


# leerPDF()
#observaciones()