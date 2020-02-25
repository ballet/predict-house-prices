from ballet import Feature
import ballet.eng


def has_qual(ser):

    return (ser == "Ex").astype(int)


input = "Fireplace Qu"

transformer = ballet.eng.SimpleFunctionTransformer(func=has_qual)

name = "Has excellent fireplace"

feature = Feature(input=input, transformer=transformer, name=name)
