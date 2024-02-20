import xml.etree.ElementTree as ET
import sys


def main():
    ############ FITXER XML ############
    # Asegúrate de proporcionar la ruta correcta del archivo XML
    tree = ET.parse('programming.xml')
    ####################################

    ############## XPATH ###############
    xpath = '/llenguatges/llenguatge/nom'
    ####################################

    # Evalúa la expresión XPath
    resultat = tree.findall(xpath)
    printXML(resultat)


# Función que imprime correctamente el resultado de la búsqueda XPath según si el resultado
# es XML, una cadena o una lista.
def printXML(xml):
    # Si es una cadena
    if isinstance(xml, str):
        print(xml)

    # Si es XML, prettyprint
    elif isinstance(xml, ET.Element):
        ET.dump(xml)

    # Si es una lista, imprime cada elemento recursivamente
    elif isinstance(xml, list):
        if not xml:
            print([])
        for x in xml:
            printXML(x)

    # Error
    else:
        print("Tipo (", type(xml), ") de ", xml, " no reconocido.")


# Función principal del programa
if __name__ == '__main__':
    main()
