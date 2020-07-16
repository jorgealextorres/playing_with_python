INSERT INTO crypto_prices.crypto_monedas(id, codi, nom, descripcio, icon_url)
values(nextval('crypto_prices.crypto_monedas_seq'), 'hola' , 'adios', 'hasta luego', 'icono');


INSERT INTO crypto_prices.monedas(id, codi, nom, descripcio) values(nextval('crypto_prices.monedas_seq'), '611', 'SixEleven', 'SixEleven (611)')

delete from crypto_prices.crypto_monedas

select * from crypto_prices.crypto_monedas

INSERT INTO crypto_prices.monedas(id, codi, nom, descripcio) values(nextval('crypto_prices.monedas_seq'), 'ZWL', 'Zimbabwean Dollar', null)

select * from crypto_prices.monedas m

delete from crypto_prices.monedas

INSERT INTO crypto_prices.crypto_prices_tab(id, data, crypto, currency, preu) values(nextval('crypto_prices.crypto_prices_tab_seq'), data, 1, 1, 3.5)

select codi, id from crypto_prices.crypto_monedas cm

select codi, id from crypto_prices.monedas m

INSERT INTO crypto_prices.crypto_prices_tab(id, data, crypto, currency, preu) values(nextval('crypto_prices.crypto_prices_seq'), '07/16/2020 19:13:05', 388, 47, 52.620498)

select tab.*, cm.id, cm.codi, m.id, m.codi
from crypto_prices.crypto_prices_tab tab
inner join crypto_prices.crypto_monedas cm on cm.id = tab.crypto
inner join crypto_prices.monedas m on m.id = tab.currency

delete from crypto_prices.crypto_prices_tab
