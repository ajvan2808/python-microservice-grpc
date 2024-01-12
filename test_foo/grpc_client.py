import sys

from log_helper import logger
import grpc
from recommendations.recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations.recommendations_pb2_grpc import RecommendationsStub


""" INTERACTING WITH RECOMMENDATIONS MICROSERVICE
The recommendations_pb2_grpc.py file contains the framework for a client and a server
The grpc module, which provides some functions for setting up connections to remote servers.
Then you import the RPC client stub. It’s called a stub because the client itself does not have any functionality.
It calls out to a remote server and passes the result back.
"""

# after ran main.py you can test_foo the client here by create another channel stub
logger.info('Initialize Client session to interact with Recommendation service')

# To make an RPC request
# You create a connection to localhost, your own machine, on port 50051.
# This port is the standard port for gRPC, but you could change it if you like.
# You’ll use an insecure channel for now, which is unauthenticated and unencrypted
channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)
request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
logger.info(f'Sent request: {request}')
response = client.Recommend(request)
if grpc.StatusCode.OK:
    logger.info(f'Request status {grpc.StatusCode.OK}')
    for recommendation in response.recommendations:
        logger.info(f'Book recommended: {recommendation}')
    sys.exit()
else:
    logger.warn(grpc.StatusCode)
    sys.exit()
