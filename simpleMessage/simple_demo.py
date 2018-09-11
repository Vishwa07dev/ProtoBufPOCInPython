import simpleMessage.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()

simple_message.id=1
simple_message.is_simple = True
simple_message.name = "Sample Name"
simple_list = simple_message.sample_list
simple_list.append(1)
simple_list.append(2)

print simple_message