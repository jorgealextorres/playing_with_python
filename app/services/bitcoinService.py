import app.repositories.bitcoinRepository
from app.repositories.bitcoinRepository import BitcoinRepository

class BitcoinService():
    def __init__(self):
        self.bitcoinRepository = BitcoinRepository()

    def getBitcoin(self):        
        return self.bitcoinRepository.getBitcoin()






