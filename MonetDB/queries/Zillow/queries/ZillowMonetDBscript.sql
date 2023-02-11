CREATE OR REPLACE FUNCTION extractba(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    import math
    array = []
    for val in x:
        try:
            max_idx = val.find(' ba')
            if max_idx < 0:
                max_idx = len(val)
            s = val[:max_idx]
            split_idx = s.rfind(',')
            if split_idx < 0:
                split_idx = 0
            else:
                split_idx += 2
            r = s[split_idx:]
            ba = math.ceil(2.0 * float(r)) / 2.0
            array.append(int(ba))
        except:
            array.append(-1)
    return array
};


CREATE OR REPLACE FUNCTION extractbd(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    array = []
    for val in x:
        try:
            max_idx = val.find(' bd')
            if max_idx < 0:
                max_idx = len(val)
            s = val[:max_idx]
            split_idx = s.rfind(',')
            if split_idx < 0:
                split_idx = 0
            else:
                split_idx += 2
            r = s[split_idx:]
            array.append(int(r))
        except:
            array.append(-1)
    return array
};


CREATE OR REPLACE FUNCTION extractid(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    import re
    array = []
    for val in x:
        match = re.search("(\d+)_zpid/$",val)
        try:
            array.append(int(match.group(1)))
        except:
            array.append(0)
    return array
};


CREATE OR REPLACE FUNCTION extractpcode(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    array = []
    for val in x:
        try:
            array.append('%05d' % int(val))
        except:
            array.append('')
    return array
};


CREATE OR REPLACE FUNCTION extractprice_sell(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    array = []
    for val in x:
        try:
            array.append(int(val[1:].replace(',', '')))
        except:
            array.append(-1)
    return array
};


CREATE OR REPLACE FUNCTION extractsqfeet(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    array = []
    for val in x:
        try:
            max_idx = val.find(' sqft')
            if max_idx < 0:
                max_idx = len(val)
            s = val[:max_idx]
            split_idx = s.rfind('ba ,')
            if split_idx < 0:
                split_idx = 0
            else:
                split_idx += 5
            r = s[split_idx:]
            r = r.replace(',', '')
            array.append(int(r))
        except:
            array.append(-1)
    return array
};


CREATE OR REPLACE FUNCTION extracttype(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    array = []
    for val in x:
        try:
            t = val.lower()
            type = 'unknown'
            if 'condo' in t or 'apartment' in t:
                type = 'condo'
            if 'house' in t:
                type = 'house'
            array.append(type)
        except:
            array.append('null')
    return array
};


DROP TABLE zillow_results;


create temp table zillow_results as
    SELECT *
    FROM (
        SELECT ba, url, address, postal_code, bds, city, state, offer, type1, sqfeet, price
        FROM (
            SELECT url, address, postal_code, bds, ba, city, state, offer, type1, sqfeet,
                CASE WHEN offer = 'sale' THEN extractprice_sell(price) ELSE 0 END AS price
            FROM (
                SELECT price, url, address, postal_code, bds, ba, city, state, offer, type1, extractsqfeet(facts_and_features) AS sqfeet
                    FROM (
                        SELECT title, address, city, state, postal_code, price, facts_and_features, type1, real_estate_provider, url, bds,
                            CASE WHEN title LIKE '%sale%' THEN 'sale'
                                 WHEN title LIKE '%sold%' THEN 'sold'
                                 WHEN title LIKE '%rent%' THEN 'rent'
                                 WHEN title LIKE '%forclose%' THEN 'forclosed' END  AS offer,
                            extractba(facts_and_features) AS ba
                        FROM (
                            SELECT title, address, city, state, postal_code, price, facts_and_features,
                                   real_estate_provider, url, type1, extractbd(facts_and_features) AS bds
                            FROM (
                                SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url, type1
                                FROM (
                                    SELECT title, address, city, state, extractpcode(postal_code) AS postal_code, price,
                                           facts_and_features, real_estate_provider, url, extracttype(title) AS type1
                                    FROM (
                                        SELECT *
                                        FROM zillow
                                        ) Z
                                    ) T
                                WHERE  type1 = 'condo'
                                ) P
                            ) S
                        WHERE  bds < 10
                    ) Q
                ) I
            ) A
        WHERE  price < 20000000 AND price > 100000
        ) H
    on commit preserve rows;


SELECT * FROM zillow_results;


CREATE OR REPLACE FUNCTION to_lower(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import string
    array = []
    for val in x:
        array.append(val.lower())
    return array
};


CREATE OR REPLACE FUNCTION strip(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import string
    array = []
    for val in x:
        array.append(val.strip())
    return array
};


CREATE OR REPLACE FUNCTION replace_o_a(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import string
    array = []
    for val in x:
        array.append(val.replace('o', 'a'))
    return array
};


SELECT SUM(bathrooms) AS sum_ba,
       SUM(sqft) AS sum_sqft,
       COUNT(url) AS urls,
       COUNT(offer) AS offers,
       COUNT(zip_code) AS zip_codes
FROM
    (
        SELECT t.bedrooms,
               extractba(t.facts_and_features) AS bathrooms,
               extractsqfeet(t.facts_and_features) AS sqft,
               extractpcode(t.postal_code) AS zip_code,
               replace_o_a(strip(to_lower(t.url))) AS url,
               extracttype(t.title) AS offer
        FROM (
            SELECT extractbd(facts_and_features) AS bedrooms,
                   extractprice_sell(price) AS price_n, *
            FROM zillow
        ) AS t
        WHERE t.bedrooms < 10 AND t.price_n > 100000 AND t.price_n < 20000000
    ) AS t
GROUP BY t.bedrooms;