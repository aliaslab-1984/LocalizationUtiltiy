import xml.etree.ElementTree as ET
import re

# Android stuff
def formatXML(key, value):
    # gestire ' con \'
    if isNaN(value):
        value = "- ToDo -"
    value = toAndroidFormat(value)
    return '\t<string name="%s">%s</string>'%(key, value.replace("'", "\'").replace("’", "\'").replace("…", "&#8230;").replace("...", "&#8230;"))

def invertXMLSpecialCharacters(inputString):
    return inputString.replace("\\'", "'").replace("\?", "?").replace("\@", "@").replace("&#8230;", "…")

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
        value = transformAndroidormattedString(child.text)
        value = invertXMLSpecialCharacters(value)
        values.append(value)
        keys.append(child.attrib["name"])
    
    return (keys, values)


def transformAndroidormattedString(value):
    processedText = re.sub('\%\d\$d', '%f', value)
    processedText = re.sub('\%\d\$s', '%s', processedText)
    return processedText

def toAndroidFormat(value):
    matches = enumerate(re.finditer('\%\w', value))
    reprocessedTextAndroid = value
    for match in matches:
        matched = match[1]
        toAndroidFormat = matched.group().replace("%", "").replace("f", "d")
        reprocessedTextAndroid = reprocessedTextAndroid.replace(matched.group(), "%{0}${1}".format(match[0] + 1, toAndroidFormat), 1)
    return reprocessedTextAndroid

#iOS Stuff

def formatiOSString(key, value):
    return '"%s" = "%s";'%(key, toiOSFormat(value))

def extractiOSKeyAndValue(element):
    elements = element.split(' = ')
    # print("Parsed elements: ", elements)
    if len(elements) < 2:
        return
    key = elements[0].replace('"', "")
    value = elements[1].replace('"', "").rstrip(" \n;")
    return (key, transformiOSFormattedString(value))

def transformiOSFormattedString(value):
    matches = enumerate(re.finditer('\%\w', value))
    reprocessedTextiOS = value
    for match in matches:
        matched = match[1]
        toiOS = matched.group().replace("@", "s").replace("d", "f")
        reprocessedTextiOS = reprocessedTextiOS.replace(matched.group(), "{}".format(toiOS), 1)
    
    return reprocessedTextiOS

def toiOSFormat(value):
    matches = enumerate(re.finditer('\%\w', value))
    reprocessedTextiOS = value
    for match in matches:
        matched = match[1]
        toiOS = matched.group().replace("s", "@").replace("f", "d")
        reprocessedTextiOS = reprocessedTextiOS.replace(matched.group(), "{}".format(toiOS), 1)
    return reprocessedTextiOS

def isNaN(num):
    return num != num