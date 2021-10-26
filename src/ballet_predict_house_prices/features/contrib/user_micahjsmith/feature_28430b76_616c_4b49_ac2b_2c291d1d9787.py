from ballet import Feature

input = "Pool Area"
transformer = lambda ser: ser.fillna(0)
name = "Pool area cleaned"
feature = Feature(input, transformer, name)
