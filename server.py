from flask import Flask, render_template

class Server:
    def __init__(self):
        self.progress = "Un-initialized"
        self.html_add = ""
        self.app = Flask(__name__)


        @self.app.route("/")
        def index():
            return render_template('template.html')


        @self.app.route("/status")
        def status():
            return self.progress

    def serve(self):
        self.app.run()