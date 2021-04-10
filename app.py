from flask import Flask, render_template, request, url_for, redirect
from test import Wallet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def wallet():
  wallet = Wallet()
  if request.method == 'GET':
    return render_template('wallet.html', wallet=wallet)
  if request.method == 'POST':
    send_address = request.form.get('send_address')
    value = request.form.get('value')
    tx = wallet.send(send_address, value)
    return render_template('send.html', send_address=send_address, value=value)

if __name__ == '__main__':
  app.run(debug=True)

  