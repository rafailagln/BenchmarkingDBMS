create table if not exists zillow_2
(
    title                varchar(256),
    address              varchar(256),
    city                 varchar(256),
    state                varchar(256),
    postal_code          INTEGER,
    price                varchar(256),
    facts_and_features   varchar(256),
    real_estate_provider varchar(256),
    url                  varchar(256)
);

INSERT INTO zillow_2 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow;
INSERT INTO zillow_2 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow;

create table if not exists zillow_4
(
    title                varchar(256),
    address              varchar(256),
    city                 varchar(256),
    state                varchar(256),
    postal_code          INTEGER,
    price                varchar(256),
    facts_and_features   varchar(256),
    real_estate_provider varchar(256),
    url                  varchar(256)
);

INSERT INTO zillow_4 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_2;
INSERT INTO zillow_4 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_2;

create table if not exists zillow_8
(
    title                varchar(256),
    address              varchar(256),
    city                 varchar(256),
    state                varchar(256),
    postal_code          INTEGER,
    price                varchar(256),
    facts_and_features   varchar(256),
    real_estate_provider varchar(256),
    url                  varchar(256)
);

INSERT INTO zillow_8 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_4;
INSERT INTO zillow_8 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_4;

create table if not exists zillow_16
(
    title                varchar(256),
    address              varchar(256),
    city                 varchar(256),
    state                varchar(256),
    postal_code          INTEGER,
    price                varchar(256),
    facts_and_features   varchar(256),
    real_estate_provider varchar(256),
    url                  varchar(256)
);

INSERT INTO zillow_16 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_8;
INSERT INTO zillow_16 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_8;

create table if not exists zillow_32
(
    title                varchar(256),
    address              varchar(256),
    city                 varchar(256),
    state                varchar(256),
    postal_code          INTEGER,
    price                varchar(256),
    facts_and_features   varchar(256),
    real_estate_provider varchar(256),
    url                  varchar(256)
);

INSERT INTO zillow_32 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_16;
INSERT INTO zillow_32 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_16;


SELECT COUNT(*) from zillow;
SELECT COUNT(*) from zillow_2;
SELECT COUNT(*) from zillow_4;
SELECT COUNT(*) from zillow_8;
SELECT COUNT(*) from zillow_16;
SELECT COUNT(*) from zillow_32;