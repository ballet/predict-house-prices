from ballet import Feature
import ballet.eng


input = ['LotArea', 'GrLivArea', 'GarageArea']
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ser['LotArea'] - ser['GrLivArea'] - ser['GarageArea'])
name = "Total green area"
feature = Feature(input=input, transformer=transformer, name=name)
