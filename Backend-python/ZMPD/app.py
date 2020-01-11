import random
import threading
import time

from flask import Flask
from flask_cors import CORS






exporting_threads = {}
app = Flask(__name__)
app.debug = True
CORS(app)



if __name__ == '__main__':
    app.run()