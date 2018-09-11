#!/usr/bin/env/ bash

protoc -I=simpleMessage/ --python_out=simpleMessage/ simpleMessage/simple.proto

protoc -I=EnumExample/ --python_out=EnumExample/ EnumExample/enum_example.proto

protoc -I=ComplexMessage/ --python_out=ComplexMessage/ ComplexMessage/complex.proto