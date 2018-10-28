from flask import Flask, render_template
from lib import html

class Server:
    def __init__(self):
        self.progress = "Un-initialized"
        self.html_add = ""
        self.app = Flask(__name__)
        self.html = html

        @self.app.route("/")
        def index():
            return render_template('template.html', html = self.html)

        @self.app.route("/result")
        def result():
            return self.html_add

        @self.app.route("/status")
        def status():
            return self.progress

    def serve(self):
        self.app.run()