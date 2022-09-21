# karrotmarket-grpc-search
This is the source that transmits the search packet of the carrot market app by Python.

## How to use

1. Install dependencies


```
$ pip3 install -r requirements.txt
```


2. Generate python code by protocol buffer compiler


```
$ python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./search.proto
$ python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./response.proto
```

  If the grpc_tools does not work, you can install protoc by following the guide [here](https://developers.google.com/protocol-buffers/docs/reference/python-generated).
  
  If successfully generated, the _pb2 file will be created in the path of the source code


3. Decode data

  Currently, this source is not complete, so you will have to run the decode yourself by command below.

```
$ protoc --decode=response.Response response.proto < response.bin
```

