from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(api_blueprint)
app.register_blueprint(website_blueprint)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'


if __name__ == "__main__":
    app.run(debug=True)
