CREATE TABLE zillow_2 (
    title varchar,
    address varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    price varchar,
    facts_and_features varchar,
    real_estate_provider varchar,
    url varchar
);

INSERT INTO zillow_2 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow;
INSERT INTO zillow_2 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow;

CREATE TABLE zillow_4 (
    title varchar,
    address varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    price varchar,
    facts_and_features varchar,
    real_estate_provider varchar,
    url varchar
);

INSERT INTO zillow_4 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_2;
INSERT INTO zillow_4 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_2;

CREATE TABLE zillow_8 (
    title varchar,
    address varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    price varchar,
    facts_and_features varchar,
    real_estate_provider varchar,
    url varchar
);

INSERT INTO zillow_8 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_4;
INSERT INTO zillow_8 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_4;

CREATE TABLE zillow_16 (
    title varchar,
    address varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    price varchar,
    facts_and_features varchar,
    real_estate_provider varchar,
    url varchar
);

INSERT INTO zillow_16 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_8;
INSERT INTO zillow_16 (title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url)
SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url FROM zillow_8;

CREATE TABLE zillow_32 (
    title varchar,
    address varchar,
    city varchar,
    state varchar,
    postal_code varchar,
    price varchar,
    facts_and_features varchar,
    real_estate_provider varchar,
    url varchar
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