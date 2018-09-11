import EnumExample.enum_example_pb2 as enum_pb2

enum_message = enum_pb2.EnumMessage()

enum_message.id = 57
enum_message.day = enum_pb2.MONDAY

print enum_message

with open("enum.bin", "wb") as f:
    print "Writing the enum example to file"
    enum_message_as_byte = enum_message.SerializeToString()
    f.write(enum_message_as_byte)
    f.close()

with open("enum.bin" , "rb") as f :
    print "Reading the enum example from file"
    enum_message_from_file = enum_pb2.EnumMessage.FromString(f.read())
    print enum_message_from_file
    f.close()