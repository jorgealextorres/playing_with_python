CREATE SEQUENCE crypto_prices.crypto_monedas_seq START with 1 INCREMENT BY 1;

CREATE TABLE crypto_prices.crypto_monedas(
	id NUMERIC(25) NOT NULL,
	codi varchar(25) NOT NULL,
	nom varchar(100) NOT NULL,
	descripcio varchar(250),
	icon_url varchar(500));

ALTER TABLE crypto_prices.crypto_monedas ADD CONSTRAINT crypto_monedas_pk PRIMARY key(id);


CREATE SEQUENCE crypto_prices.monedas_seq START with 1 INCREMENT BY 1;

CREATE TABLE crypto_prices.monedas(
	id NUMERIC(25) NOT NULL,
	codi varchar(25) NOT NULL,
	nom varchar(100) NOT NULL,
	descripcio varchar(250));

 ALTER TABLE crypto_prices.monedas ADD CONSTRAINT monedas_pk PRIMARY key(id);


CREATE SEQUENCE crypto_prices.crypto_prices_seq START with 1 INCREMENT BY 1;

CREATE TABLE crypto_prices.crypto_prices_tab(
	id NUMERIC(25) NOT NULL,
	data timestamp NOT NULL,
	crypto NUMERIC(25) NOT NULL,
	currency NUMERIC(25) NOT NULL,
	preu NUMERIC(10,2) NOT NULL);

ALTER TABLE crypto_prices.crypto_prices_tab ADD CONSTRAINT crypto_prices_tab_pk PRIMARY key(id);
ALTER TABLE crypto_prices.crypto_prices_tab ADD CONSTRAINT crypto_prices_tab_fk1 FOREIGN KEY(crypto) REFERENCES crypto_prices.crypto_monedas(id);
ALTER TABLE crypto_prices.crypto_prices_tab ADD CONSTRAINT crypto_prices_tab_fk2 FOREIGN KEY(currency) REFERENCES crypto_prices.monedas(id);
