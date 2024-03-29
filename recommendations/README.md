### To generate Python code from the protobufs, run the following:
`cd recommendations` <br> 
`python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto`

The two will be generated by the cmd above. These files include Python types and functions to interact with your API. The compiler will generate client code to call an RPC and server code to implement the RPC.
- `recommendations_pb2.py` : contains types definitions, the protobuf compiler generated Python types corresponding to your protobuf types.
- `recommendations_pb2_grpc.py`: contains the framework for a client and a server


* `python -m grpc_tools.protoc` runs the protobuf compiler, which will generate Python code from the protobuf code. \
* `-I ../protobufs` tells the compiler where to find files that your protobuf code imports. You don’t actually use the import feature, but the -I flag is required nonetheless. \
* `--python_out=. --grpc_python_out=.` tells the compiler where to output the Python files. As you’ll see shortly, it will generate two files, and you could put each in a separate directory with these options if you wanted to.\
* `../protobufs/recommendations.proto` is the path to the protobuf file, which will be used to generate the Python code.

Other resources: 
- `services.py`: contains Recommendation Service functions implementation.
- `run_services.py`: establishes network server and use microservice class to handle request 
- `data.py`: create some sample data