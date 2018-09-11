import simpleMessage.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()

simple_message.id=1
simple_message.is_simple = True
simple_message.name = "Sample Name"
#List can't be directly added. It has first to be taken out and then added.
simple_list = simple_message.sample_list
simple_list.append(1)
simple_list.append(2)

print simple_message


with open("simple.bin" , "wb")  as f :
    print "writing data to the file"
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)

with open("simple.bin", "rb") as f :
    print "Reading data from the file"
    simple_message_from_file = simple_pb2.SimpleMessage().FromString(f.read())
    print simple_message_from_file
