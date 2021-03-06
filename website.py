from flask import Flask, render_template
from threading import Thread
import sys
app = Flask('')




@app.route("/")
def index():
	return render_template("index.html")

@app.route("/commands")
def commandsHelp():
	return render_template("commands_help.html")

def run():
    app.run(host="0.0.0.0")

def start():
    server = Thread(target=run)
    server.start()

def shutdownserver():
    sys.exit()

def shutdownasync():
    shutdown = Thread(target=shutdownserver)
    shutdown.start()


