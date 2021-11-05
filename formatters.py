# Android stuff
def formatXML(key, value):
    return '\t<string name="%s">%s</string>'%(key, value)

def xmlHeaderString():
    return "<resources>"

def xmlFooterString():
    return "</resources>"

#iOS Stuff

def formatiOSString(key, value):
    return '"%s" = "%s";'%(key, value)
