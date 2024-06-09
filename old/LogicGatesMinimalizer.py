a = ['~x1', '~x3', 'x0x2', '~x0~x2']
b = ['x2', '~x0~x1', 'x0x1']
c = ['~x0', 'x1', '~x2']
d = ['~x3', ['x0~x1x2'], 'x1~x2', ['x0', '~x1x2']]
e = ['~x0', '~x1x2']
f = ['~x0~x1', '~x2', '~x3']
g = ['~x1x2', '~x3', ['x1', 'x0x2']]

logicFuntions = []
minimalizedFunctions = []


def minimalize(array, logicFunctions, minimalizedFunctions):
    for element in array:
        if (isinstance(element, list)):
            for subelement in element:
                if (subelement not in logicFunctions):
                    logicFunctions.append(subelement)
                else:
                    if (len(subelement) > 3):
                        minimalizedFunctions.append(subelement)
                    else:
                        logicFunctions.append(subelement)

        else:
            if (element not in logicFunctions):
                logicFunctions.append(element)
            else:
                if (len(element) > 3):
                    minimalizedFunctions.append(element)
                else:
                    logicFunctions.append(element)


minimalize(a, logicFuntions, minimalizedFunctions)
minimalize(b, logicFuntions, minimalizedFunctions)
minimalize(c, logicFuntions, minimalizedFunctions)
minimalize(d, logicFuntions, minimalizedFunctions)
minimalize(e, logicFuntions, minimalizedFunctions)
minimalize(f, logicFuntions, minimalizedFunctions)
minimalize(g, logicFuntions, minimalizedFunctions)

print(logicFuntions)
print(minimalizedFunctions)
