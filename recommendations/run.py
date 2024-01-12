import grpc
from concurrent import futures
import recommendations_pb2_grpc
from services import RecommendationService
from log_helper import logger
from grpc_interceptor import ExceptionToStatusInterceptor
from signal import signal, SIGTERM

"""
Starts a network server and uses your microservice class to handle requests
1. creates a gRPC server. Use 10 threads to serve requests good default for an actual Python microservice.
2. associates your class with the server. This is like adding a handler for requests.
3. tells the server to run on standard port 50051.
4. call server.start() and server.wait_for_termination() to start the microservice and wait until it’s stopped manually.
"""


def run_server():
    # If one of the exceptions is raised by the microservice, then ExceptionToStatusInterceptor will set the gRPC status code.
    interceptor = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptor)
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(RecommendationService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    logger.info("Service started!")

    # Handling shutdown gracefully
    def handle_sigterm(*_):
        logger.info("Received shutdown signal")
        # shut down the server gracefully. It will refuse new requests and wait 30 seconds for current requests to complete.
        # It returns immediately, but it returns a threading.Event object on which you can wait.
        all_rpc_done_event = server.stop(30)
        all_rpc_done_event.wait(30)  # waits on the Event object so Python doesn’t exit prematurely
        logger.info("Shutdown gracefully!")

    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()


if __name__ == '__main__':
    logger.info("Start gRPC server. Recommendations service is running")
    run_server()
