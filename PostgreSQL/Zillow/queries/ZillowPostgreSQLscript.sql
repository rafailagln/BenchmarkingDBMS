create function extractba(val character varying) returns integer
    language plpython3u
as
$$
    import math
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
        return int(ba)
    except:
        return -1
$$;

alter function extractba(varchar) owner to postgres;


create function extractbd(val character varying) returns integer
    language plpython3u
as
$$
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
        return int(r)
    except:
        return -1
$$;

alter function extractbd(varchar) owner to postgres;


create function extractid(val character varying) returns integer
    language plpython3u
as
$$
    import re
    match = re.search("(\d+)_zpid/$",val)
    try:
        return int(match.group(1))
    except:
        return  0
$$;

alter function extractid(varchar) owner to postgres;


create function extractpcode(val integer) returns text
    language plpython3u
as
$$
    try:
        return '%05d' % int(val)
    except:
        return ''
$$;

alter function extractpcode(integer) owner to postgres;


create function extractprice_sell(val character varying) returns integer
    language plpython3u
as
$$
    try:
        return  int(val[1:].replace(',', ''))
    except:
        return -1
$$;

alter function extractprice_sell(varchar) owner to postgres;


create function extractsqfeet(val character varying) returns integer
    language plpython3u
as
$$
    try:
        max_idx = val.find(' sqft')
        if max_idx < 0:
            max_idx = len(val)
        s = val[:max_idx]
        split_idx = s.rfind('ba ,')
        if split_idx < 0:
            split_idx = 0
        else:
            split_idx += 4
        r = s[split_idx:]
        r = r.replace(',', '')
        return int(r)
    except:
        return -1
$$;

alter function extractsqfeet(varchar) owner to postgres;


create function extracttype(val character varying) returns text
    language plpython3u
as
$$
    try:
        t = val.lower()
        type = 'unknown'
        if 'condo' in t or 'apartment' in t:
            type = 'condo'
        if 'house' in t:
            type = 'house'
        return  type
    except:
        return 'null'
$$;

alter function extracttype(varchar) owner to postgres;




DROP TABLE zillow_results;

create temp table zillow_results on commit preserve rows as
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
    ) H;

SELECT * FROM zillow_results;


create function to_lower(val character varying) returns text
    language plpython3u
as
$$
    import string
    return val.lower()
$$;

alter function to_lower(varchar) owner to postgres;


create function strip(val character varying) returns text
    language plpython3u
as
$$
    import string
    return val.strip()
$$;

alter function strip(varchar) owner to postgres;


create function replace_o_a(val character varying) returns text
    language plpython3u
as
$$
    import string
    return val.replace('o', 'a')
$$;

alter function replace_o_a(varchar) owner to postgres;


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
