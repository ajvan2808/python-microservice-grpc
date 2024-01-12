from flask import Flask, render_template
from marketplace import RecommendationRequest, BookCategory, rcmdt_client
app = Flask(__name__)


@app.route('/')
def homepage():
    recomdt_request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    recomdt_response = rcmdt_client.Recommend(recomdt_request)

    return render_template(
        "homepage.html",
        recommendations=recomdt_response.recommendations,
    )
