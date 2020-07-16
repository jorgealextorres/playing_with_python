import urllib.request
import json
from jsonpath_ng import jsonpath, parse
import psycopg2

def crypto_info_web2localDatabase():
    urlData = "http://api.coinlayer.com/list?access_key=bbe857e49a4fbaba79476ebc72e36493"
    conn = None

    try:
        conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="password")
        cur = conn.cursor()

        webUrl = urllib.request.urlopen(urlData)
        print ("result code: " + str(webUrl.getcode()))
        if (webUrl.getcode() == 200):
            data = webUrl.read()
            theJSON = json.loads(data)

            jsonpath_expression = parse('$..symbol')
            for match in jsonpath_expression.find(theJSON):
                print("INSERT INTO crypto_prices.crypto_monedas(id, codi, nom, descripcio, icon_url) values(nextval('crypto_prices.crypto_monedas_seq'), '" + theJSON["crypto"][match.value]["symbol"] + "', '" + theJSON["crypto"][match.value]["name"] + "', '" + theJSON["crypto"][match.value]["name_full"] + "', '" + theJSON["crypto"][match.value]["icon_url"] + "')")
                cur.execute("INSERT INTO crypto_prices.crypto_monedas(id, codi, nom, descripcio, icon_url) values(nextval('crypto_prices.crypto_monedas_seq'), '" + theJSON["crypto"][match.value]["symbol"] + "', '" + theJSON["crypto"][match.value]["name"] + "', '" + theJSON["crypto"][match.value]["name_full"] + "', '" + theJSON["crypto"][match.value]["icon_url"] + "')")

            conn.commit()
        else:
            print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def monedas_info_web2localDatabase():
    urlData = "http://api.coinlayer.com/list?access_key=bbe857e49a4fbaba79476ebc72e36493"
    conn = None

    try:
        conn = psycopg2.connect(host="localhost",database="postgres", user="postgres", password="password")
        cur = conn.cursor()

        webUrl = urllib.request.urlopen(urlData)
        print ("result code: " + str(webUrl.getcode()))
        if (webUrl.getcode() == 200):
            data = webUrl.read()
            theJSON = json.loads(data)
            theMonedasJson = theJSON["fiat"]

            for key in theMonedasJson:
                print("INSERT INTO crypto_prices.monedas(id, codi, nom, descripcio) values(nextval('crypto_prices.monedas_seq'), '" + key + "', '" + theMonedasJson[key] + "', null)")
                cur.execute("INSERT INTO crypto_prices.monedas(id, codi, nom, descripcio) values(nextval('crypto_prices.monedas_seq'), '" + key + "', '" + theMonedasJson[key] + "', null)")

            conn.commit()
        else:
            print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')