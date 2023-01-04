SELECT * FROM
    (SELECT ba, url, address, postal_code, bds, city, state, offer, type1, sqfeet, price
        FROM   (SELECT url, address, postal_code, bds, ba, city, state, offer, type1, sqfeet,
                       CASE WHEN offer = 'sale' THEN extractprice_sell(price) ELSE '0' END AS price
                FROM   (SELECT price, url, address, postal_code, bds, ba, city, state, offer, type1,
                               extractsqfeet(facts_and_features) AS sqfeet
                        FROM   (SELECT title, address, city, state, postal_code, price, facts_and_features, type1, real_estate_provider, url, bds,
                                       CASE WHEN title LIKE '%sale%' THEN 'sale' WHEN title LIKE '%sold%' THEN 'sold' WHEN title LIKE '%rent%' THEN 'rent'
                                         WHEN title LIKE '%forclose%' THEN 'forclosed' END  AS offer,
                                       extractba(facts_and_features) AS ba
                                FROM   (SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url, type1,
                                               extractbd(facts_and_features) AS bds
                                        FROM   (SELECT title, address, city, state, postal_code, price, facts_and_features, real_estate_provider, url, type1
                                                FROM   (SELECT title, address, city, state, extractpcode(postal_code) AS postal_code, price, facts_and_features,
                                                                real_estate_provider, url, extracttype(title) AS type1
                                                        FROM   (SELECT * FROM zillow) Z) T
                                                          WHERE  type1 = 'condo') p) S
                                                 WHERE  bds < 10) Q) I) A
               WHERE  price < 20000000 AND price > 100000) H;