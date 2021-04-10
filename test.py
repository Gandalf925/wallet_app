from bitsv import Key

class Wallet:
  def __init__(self):

    self.key = Key('cVYfBhkScsUdtNi7Lckx1rehj89Hx2eJUMYD2k2RQ5KqPg4BydWb', network='test')

    self.key.get_balance()
    self.address = self.key.address
    self.bal = self.key.get_balance('bsv')
    self.jpy_bal = self.key.balance_as('jpy')
  
  def send(self, send_address, value):
    output = [(
      send_address,
      value,
      'jpy'
    )]
    self.key.send(output)


if __name__ == '__main__':
  second_key = Key("cUYv2Nj9YgxWNPKrdnLhyCC4KfUMjyXh623K5tv2kHrT6EDcwscE", network='test')
  print(second_key.address)
  second_key.get_balance()
  print(second_key.balance_as('jpy') + '円')
