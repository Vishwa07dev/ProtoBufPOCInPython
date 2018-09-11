import complex_pb2 as complex_pb2

complex_object = complex_pb2.ComplexObject()
complex_object.id=77
#Object can't be directly assigned. It has to be retrieved and then value has to be set as like in list
child_object = complex_object.childObject
child_object.id = 100
child_object.name = "Vishwa"
complex_object.brand = complex_pb2.HIGH_BRAND


print(complex_object)

with open("complex.bin" , "wb") as f :
    print "Writing the complex message to file"
    complex_object_bytes = complex_object.SerializeToString()
    f.write(complex_object_bytes)
    f.close()

with open("complex.bin" ,"rb") as f :
    print "Reading message from the file"
    complex_object_from_file = complex_pb2.ComplexObject.FromString(f.read())
    print complex_object_from_file
    f.close()


