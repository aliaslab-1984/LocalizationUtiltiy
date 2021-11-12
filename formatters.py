import xml.etree.ElementTree as ET

# Android stuff
def formatXML(key, value):
    # gestire ' con \'
    return '\t<string name="%s">%s</string>'%(key, value.replace("'", "\'").replace("…", "&#8230;").replace("...", "&#8230;"))

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
    key = elements[0].replace('"', "")
    value = elements[1].replace('"', "").replace(";", "").replace("&#8230;", "…").rstrip()
    return (key, value)
