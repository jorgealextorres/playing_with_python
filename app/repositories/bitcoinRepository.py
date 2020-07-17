from app.application import App
import psycopg2
from psycopg2.extras import RealDictCursor


class BitcoinRepository():
    def getBitcoin(self):
        conn = None

        try:
            conn = App.connectionPool.getconn()
            cur = conn.cursor(cursor_factory=RealDictCursor)

            cur.execute("SELECT data, preu from crypto_prices.crypto_prices_tab cpt where cpt.crypto = 445 order by 1")
            bitcoin_records = cur.fetchall()

            cur.close()

            return bitcoin_records

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if conn is not None:
                App.connectionPool.putconn(conn)
        