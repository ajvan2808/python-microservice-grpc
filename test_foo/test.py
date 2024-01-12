""" RECOMMENDATIONS_PB2.PY
The recommendations_pb2.py file that was generated for you contains the type definitions
the protobuf compiler generated Python types corresponding to your protobuf types.
"""

from recommendations.recommendations_pb2 import BookCategory, RecommendationRequest

request0 = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
print(request0.category)
# >>> 1


""" There’s some type checking on the fields """
try:
    request1 = RecommendationRequest(user_id="oops", category=BookCategory.SCIENCE_FICTION, max_results=3)
except Exception as err:
    print(err)

"""
Note: that all fields in proto3 are optional, so you’ll need to validate that they’re all set.
If you leave one unset, then it’ll default to zero for numeric types or to an empty string for strings
"""
request2 = RecommendationRequest(user_id=2, category=BookCategory.SCIENCE_FICTION)
print(request2.max_results)
# >>> 0
