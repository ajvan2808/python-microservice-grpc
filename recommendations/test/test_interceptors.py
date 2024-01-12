import grpc
import pytest
from grpc_interceptor.testing import dummy_client, DummyRequest, raises
import unittest
from grpc_interceptor import ExceptionToStatusInterceptor


class MockErrorLogger(ExceptionToStatusInterceptor):

    def __init__(self):
        super().__init__()
        self.logged_exception = None

    def log_error(self, ect: Exception) -> None:
        self.logged_exception = ect


class TestInterceptor(unittest.TestCase):
    mock_error = MockErrorLogger()
    exception = Exception()
    special_cases = {"error": raises(exception)}

    def test__log_error(self):
        with dummy_client(special_cases=self.special_cases, interceptors=[self.mock_error]) as client:
            output = client.Execute(DummyRequest(input="foo")).output
            # no exception case
            self.assertEqual(output, "foo")
            self.assertEqual(self.mock_error.logged_exception, None)

            # with exception case
            with pytest.raises(grpc.RpcError) as er:
                client.Execute(DummyRequest(input="error"))

            self.assertRaises(Exception, self.mock_error.logged_exception)
