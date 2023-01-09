SELECT ip, date, method, endpoint, protocol, response_code, content_size
FROM (
        SELECT extract_ip(c1) as ip, extract_client_id(c1) as client_id,
               extract_user_id(c1) as user_id, extract_date(c1) as date,
               extract_method(c1) as method, extract_endpoint(c1) as endpoint,
               extract_protocol(c1) as protocol, extract_response_code(c1) as response_code,
               extract_content_size(c1) as content_size
        FROM weblogs
        WHERE extract_endpoint(c1) != ''
    ) as df
JOIN ip_blacklist as bad_ip_df ON df.ip = bad_ip_df.BadIPs;