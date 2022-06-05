from flask import Flask, render_template, request, redirect, make_response, url_for
from user import User, db

app = Flask(__name__)
db.create_all()


@app.route("/", methods=["GET"])
def index():

    user_email = request.cookies.get("email")

    user = None
    if user_email:
        user = db.query(User).filter_by(email=user_email).first()

    return render_template("index.html", user=user)


@app.route("/login", methods=["POST"])
def login():

    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    email = request.form.get("email")

    user = User(first_name=first_name, last_name=last_name, email=email)
    user.save()

    response = make_response(redirect(url_for("index")))
    response.set_cookie("email", user.email)

    return response


if __name__ == "__main__":
    app.run(port=5002, use_reloader=True)
