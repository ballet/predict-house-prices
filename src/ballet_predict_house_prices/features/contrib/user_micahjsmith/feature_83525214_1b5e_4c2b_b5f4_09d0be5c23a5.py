from ballet import Feature


def has_qual(ser):
    return (ser == "Ex").astype(int)


input = "Fireplace Qu"
transformer = has_qual
name = "Has excellent fireplace"
feature = Feature(input=input, transformer=transformer, name=name)
