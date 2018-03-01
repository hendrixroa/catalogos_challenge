DROP DATABASE catalogs;
CREATE DATABASE catalogs;
\c catalogs;

CREATE TABLE products(
   ID INT PRIMARY KEY NOT NULL,
   CREATED DATE,
   MODIFIED DATE,
   IS_ACTIVE BOOLEAN,
   TYPE CHAR(100),
   NAME CHAR(100),
   DESCRIPTION CHAR(500),
   IS_VARIATION BOOLEAN,
   BRAND_ID INT,
   CODE INT,
   FAMILY INT,
   IS_COMPLEMENT BOOLEAN,
   IS_DELETE BOOLEAN
);

CREATE TABLE products_detail (
    ID INT PRIMARY KEY NOT NULL,
    CREATED DATE,
    MODIFIED DATE,
    IS_ACTIVE BOOLEAN,
    IS_VISIBILITY BOOLEAN,
    PRICE FLOAT,
    PRICE_OFFER FLOAT,
    OFFER_DAY_FROM DATE,
    OFFER_DAY_TO DATE,
    QUANTITY INT,
    SKU INT,
    PRODUCT_ID INT
);

/*
Recuerda cambiar por la ruta en donde ejecutaras el proyecto
*/
\COPY products FROM '/home/hendrix/ProyectosPython/catalogos_challenge/instalacion/plantilla_producto.csv' WITH CSV HEADER;
\COPY products_detail FROM '/home/hendrix/ProyectosPython/catalogos_challenge/instalacion/plantilla_detalle.csv' WITH CSV HEADER;