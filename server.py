from flask import Flask, render_template, make_response
from lib import html

class Server:
    def __init__(self):
        self.progress = "Un-initialized"
        self.html_add = ""
        self.app = Flask(__name__)
        self.html = html
        self.status = 'In-progress'

        @self.app.route("/")
        def index():
            return render_template('template.html', html = self.html)

        @self.app.route("/result")
        def result():
            resp = make_response(self.html_add, 200)
            resp.headers.extend({'R-Processing':self.status})
            return resp

        @self.app.route("/status")
        def status():
            return self.progress

    def serve(self):
        self.app.run()