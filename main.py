import hashcracker
from flask import Flask, request
from two1.bitserv.flask import Payment
from two1.wallet import Wallet

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app,wallet)

@app.route('/solve')
@payment.required(1000)
def solvehash():
    run=hashcracker.Control()
    solved = run.main(request.args.get("hash"))
    if solved == None:
        return "false"
    else:
        return "true"

@app.route('/getresult')
@payment.required(10000)
def retrievehash():
    run=hashcracker.Control()
    solved = run.main(request.args.get("hash"))
    if solved:
    	return solved
    return "false"

app.run(host="0.0.0.0")
