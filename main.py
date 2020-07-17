import app.application as application
from bu_main import init
import app.bu1 as bu1
import app.runOnce as runOnce
import app.extractor as extractor

def main():
  print ("hello !!!!!! :D")

if __name__ == "__main__":
  # runOnce.crypto_info_web2localDatabase()
  # runOnce.monedas_info_web2localDatabase()

  # main()
  # init()
  # bu1.init()
  application.App.init()

  extractor.crypto_prices_web2localDatabase()
  
  application.App.finish()