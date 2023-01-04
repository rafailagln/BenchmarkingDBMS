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
               replace_o_a(to_strip(to_lower(t.url))) AS url,
               extracttype(t.title) AS offer
        FROM (
            SELECT extractbd(facts_and_features) AS bedrooms,
                   -- Added replace + -> "" because values like this "$699,900+"
                   -- exists and the udf only parsed it to 699900+
                   replace(extractprice_sell(price), '+', '') AS price_n, *
            -- Added NOT LIKE '%None%' because extractsqfeet when facts and features
            -- has None in bedrooms count not convert it to float
            FROM zillow where facts_and_features NOT LIKE '%None%'
        ) AS t
        WHERE t.bedrooms < 10 AND t.price_n > 100000 AND t.price_n < 20000000
    ) AS t
GROUP BY t.bedrooms;