from recommendations.run import run_server
from test_foo.log_helper import logger


if __name__ == '__main__':
    logger.info("Start gRPC server for test_foo Recommendations service")
    run_server()
