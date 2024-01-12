import random
import recommendations_pb2_grpc
from data import books_by_category
from recommendations_pb2 import RecommendationResponse
from grpc_interceptor.exceptions import NotFound


class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            raise NotFound("Category Not Found")
            # Handle error with grpc abort
            # context.abort(grpc.StatusCode.NOT_FOUND, "Category Not Found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)
