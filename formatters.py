import xml.etree.ElementTree as ET

# Android stuff
def formatXML(key, value):
    # gestire ' con \'
    if isNaN(value):
        value = "- ToDo -"
    return '\t<string name="%s">%s</string>'%(key, value.replace("'", r"\'").replace("…", "&#8230;").replace("...", "&#8230;"))

def invertXMLSpecialCharacters(inputString):
    return inputString.replace("\\'", "'").replace("&#8230;", "…")

def xmlHeaderString():
    return "<resources>"

def xmlFooterString():
    return "</resources>"

def extractXMLKeyAndValue(filename):
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    values = list()
    keys = list()
    for child in root:
        values.append(child.text)
        keys.append(child.attrib["name"])
    
    return (keys, values)

#iOS Stuff

def formatiOSString(key, value):
    return '"%s" = "%s";'%(key, value)

def extractiOSKeyAndValue(element):
    elements = element.split(' = ')
    # print("Parsed elements: ", elements)
    if len(elements) < 2:
        return
    key = elements[0].replace('"', "")
    value = elements[1].replace('"', "").rstrip(" \n;")
    return (key, value)

def isNaN(num):
    return num != num