import os
import grpc
from marketplace.recommendations_pb2 import BookCategory, RecommendationRequest
from marketplace.recommendations_pb2_grpc import RecommendationsStub

'''
you create the gRPC channel and stub as globals. Usually globals are a no-no, but in this case an exception is warranted.
The gRPC channel keeps a persistent connection to the server to avoid the overhead of having to repeatedly connect. 
It can handle many simultaneous requests and will reestablish dropped connections. 
However, if you create a new channel before each request, then Python will garbage collect it, 
and you won’t get most of the benefits of a persistent connection.
You want the channel to stay open so you don’t need to reconnect to the recommendations microservice for every request
'''

rcmdt_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
rcmdt_channel = grpc.insecure_channel(f"{rcmdt_host}:50051")
rcmdt_client = RecommendationsStub(rcmdt_channel)
