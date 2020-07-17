import app.application as application
import flask
from flask import request, jsonify
import app.services.bitcoinService as bitcoinService

app = flask.Flask(__name__)

@app.route('/bitcoin', methods=['GET'])
def home():
    # return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
    application.App.init()

    service = bitcoinService.BitcoinService()

    result = service.getBitcoin()

    application.App.finish()

    return jsonify(result)

app.run()