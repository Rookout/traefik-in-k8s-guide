import os

from flask import Flask

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    background_color = os.environ.get("BACKGROUND_COLOR", "powderblue")
    title = os.environ.get("TITLE", "Im in the cloud!!!")
    return """
        <!DOCTYPE html>
        <html>
        <body style="background-color:{BACKGROUND_COLOR};">

        <h1>{TITLE}</h1>
        <h2>THIS IS THE PATH: {path}</h2>
        <p>This webinar is fun</p>

        </body>
        </html>
        """.format(
        BACKGROUND_COLOR=background_color, TITLE=title,path=path
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
