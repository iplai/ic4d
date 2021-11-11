import c4d, random
from c4d.modules import mograph as mo


def main():
    moData = mo.GeGetMoData(op)
    if moData is None:
        return False

    carr = moData.GetArray(c4d.MODATA_COLOR)

    for i in range(moData.GetCount()):
        carr[i] = c4d.Vector(random.random(), random.random(), random.random())

    hasField = op[c4d.FIELDS].HasContent()

    moData.SetArray(c4d.MODATA_COLOR, carr, hasField)
    return True
