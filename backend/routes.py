from flask import current_app,jsonify,request
from app import create_app,db
from models import Articles,articles_schema

# Create an application instance
app = create_app()


@app.route("/")
def home():

    return 


# Define a route to fetch the avaialable articles
@app.route("/articles", methods=["GET"], strict_slashes=False)
def articles():

	articles = Articles.query.all()
	results = articles_schema.dump(articles)

	return jsonify(results)


# change debug to False when in prod
if __name__ == "__main__":
	app.run(debug=True)
