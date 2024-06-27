from model.model import Model

mymodel = Model()
mymodel.buildGraph(5)
print(mymodel.printGraphDetails())
print(mymodel.getVicini("Albuquerque International Sunport"))
