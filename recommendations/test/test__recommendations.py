import unittest
import grpc
from unittest import mock
from services import RecommendationService
from recommendations_pb2 import BookCategory, RecommendationRequest, BookRecommendation


class TestRecommendationService(unittest.TestCase):
    service = RecommendationService()
    context = unittest.mock.MagicMock()
    book_recommendation = BookRecommendation(id=1, title="The Maltese Falcon")

    def test_recommendations(self):
        mock_request = RecommendationRequest(user_id=0, category=BookCategory.MYSTERY, max_results=1)
        response = self.service.Recommend(mock_request, self.context)
        self.assertEqual(1, len(response.recommendations))
