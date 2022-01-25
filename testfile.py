import xml.etree.ElementTree as ET
import re

exampleString = """
<resources>
<string name=\"welcome_messages\">Hello, %1$s! You have %2$d new messages. %3$s</string>
</resources>
"""

root = ET.fromstring(exampleString)

for child in root:
    print(child.attrib["name"], "->", child.text)
    processedText = re.sub('\%\d\$d', '%f', child.text)
    processedText = re.sub('\%\d\$s', '%s', processedText)
    print(processedText)

    matches = enumerate(re.finditer('\%\w', processedText))
    reprocessedTextAndroid = processedText
    reprocessedTextiOS = processedText
    for match in matches:
        matched = match[1]
        print(matched.group())
        toAndroid = matched.group().replace("%", "").replace("f", "d")
        toiOS = matched.group().replace("s", "@") 
        reprocessedTextAndroid = reprocessedTextAndroid.replace(matched.group(), "%{0}${1}".format(match[0] + 1, toAndroid), 1)
        reprocessedTextiOS = reprocessedTextiOS.replace(matched.group(), "{}".format(toiOS), 1)
    
    print("Android ->", reprocessedTextAndroid)
    print("iOS ->", reprocessedTextiOS)