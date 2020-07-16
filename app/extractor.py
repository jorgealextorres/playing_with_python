import urllib.request
import json
from jsonpath_ng import jsonpath, parse
import psycopg2
import datetime

def crypto_prices_web2localDatabase():
    urlData = "http://api.coinlayer.com/api/live?access_key=bbe857e49a4fbaba79476ebc72e36493&target=EUR"
    conn = None
    crypto = dict()

    try:
        conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="password")
        cur = conn.cursor()

        # get the crypto codes
        cur.execute("select codi, id from crypto_prices.crypto_monedas cm ")
        crypto_records = cur.fetchall()
        for row in crypto_records:
            crypto[row[0]] = int(row[1])
 
        webUrl = urllib.request.urlopen(urlData)
        print ("result code: " + str(webUrl.getcode()))        
        if (webUrl.getcode() == 200):
            data = webUrl.read()
            theJSON = json.loads(data)

            if(theJSON["success"]):
                timestamp = datetime.datetime.fromtimestamp(int(theJSON["timestamp"]))
                print("timestamp", timestamp)
                moneda = theJSON["target"]

                # get the monedas id
                cur.execute("select id from crypto_prices.monedas m where codi = '" + moneda + "'")
                moneda_id = int(cur.fetchone()[0])

                thePricesJson = theJSON["rates"]

                for key in thePricesJson:
                    print("INSERT INTO crypto_prices.crypto_prices_tab(id, data, crypto, currency, preu) values(nextval('crypto_prices.crypto_prices_seq'), '" + timestamp.strftime("%m/%d/%Y %H:%M:%S") + "', " + str(crypto[key]) + ", " + str(moneda_id) + ", " + str(thePricesJson[key]) + ")")
                    cur.execute("INSERT INTO crypto_prices.crypto_prices_tab(id, data, crypto, currency, preu) values(nextval('crypto_prices.crypto_prices_seq'), '" + timestamp.strftime("%m/%d/%Y %H:%M:%S") + "', " + str(crypto[key]) + ", " + str(moneda_id) + ", " + str(thePricesJson[key]) + ")")

            conn.commit()
        else:
            print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')