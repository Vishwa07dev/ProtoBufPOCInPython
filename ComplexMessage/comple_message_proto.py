import complex_pb2 as complex_pb2

complex_object = complex_pb2.ComplexObject()
complex_object.id=77
#Object can't be directly assigned. It has to be retrieved and then value has to be set as like in list
child_object = complex_object.childObject
child_object.id = 100
child_object.name = "Vishwa"
complex_object.brand = complex_pb2.HIGH_BRAND


print(complex_object)

with open("complex.bin" , "wb")

