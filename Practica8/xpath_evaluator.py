from lxml import etree
from sys import stdout


def main():
        ############ FITXER XML ############
    tree = etree.parse('D:/DAM/M04/Practica8/ods.xml')
        ####################################

        ############## XPATH ###############
    xpath = '(//grup[@tipus="ambiental"]/objectiu/accions/accio)[position() <= 5]'
        ####################################
        # Evalua l'expressió XPath
    resultat = tree.xpath(xpath)
    printXML(resultat)


# Funció que imprimeix correctament el resultat de la cerca amb XPath en funció de si el resultat
# és un XML o bé un string, o bé una llista.
def printXML(xml):
    # si és string
    if type(xml) is etree._ElementUnicodeResult:
        print(xml)

    # si és xml, prettyprint
    elif type(xml) is etree._Element:
        et = etree.ElementTree(xml)
        et.write(stdout.buffer, pretty_print=True)

    # si és llista, un a un recursivament.
    elif type(xml) is list:
        if len(xml) == 0:
            print([])
        for x in xml:
            printXML(x)

    # error
    else:
        print("No es reconeix el tipus (", type(xml), ") de ", xml)


# Main del programa
if __name__ == '__main__':
    main()
