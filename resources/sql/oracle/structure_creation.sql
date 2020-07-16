CREATE SEQUENCE crypto_monedas_seq START with 1 INCREMENT BY 1;

CREATE TABLE crypto_monedas(
	id NUMBER(25) NOT NULL,
	codi varchar2(10) NOT NULL,
	nom varchar2(25) NOT NULL,
	descripcio varchar2(250),
	icon_url varchar2(250));

ALTER TABLE crypto_monedas ADD CONSTRAINT crypto_monedas_pk PRIMARY key(id);


CREATE SEQUENCE monedas_seq START with 1 INCREMENT BY 1;

CREATE TABLE monedas(
	id NUMBER(25) NOT NULL,
	codi varchar2(10) NOT NULL,
	nom varchar2(25) NOT NULL,
	descripcio varchar2(250));

 ALTER TABLE monedas ADD CONSTRAINT monedas_pk PRIMARY key(id);


CREATE SEQUENCE crypto_prices_seq START with 1 INCREMENT BY 1;

CREATE TABLE crypto_prices_tab(
	id number(25) NOT NULL,
	DATA timestamp NOT NULL,
	crypto number(25) NOT NULL,
	currency number(25) NOT NULL,
	preu number(10,2) NOT NULL);

ALTER TABLE crypto_prices_tab ADD CONSTRAINT crypto_prices_tab_pk PRIMARY key(id);
ALTER TABLE crypto_prices_tab ADD CONSTRAINT crypto_prices_tab_fk1 FOREIGN KEY(crypto) REFERENCES crypto_monedas(id);
ALTER TABLE crypto_prices_tab ADD CONSTRAINT crypto_prices_tab_fk2 FOREIGN KEY(currency) REFERENCES monedas(id);
