CREATE OR REPLACE FUNCTION extract_client_id(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    return [re.search(r"^\S+ (\S+) ", i)[1] for i in x]
};


CREATE OR REPLACE FUNCTION extract_date(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    return [re.search(r"^.*\[([\w:/]+\s[+\-]\d{4})\]", i)[1] for i in x]
};


CREATE OR REPLACE FUNCTION extract_content_size(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    import re
    array = []
    for i in x:
        match = re.search(r'^.*" \d{3} (\S+)', i)
        if match:
            if match[1] == '-':
                array.append(0)
            else:
                array.append(int(match[1]))
        else:
            array.append(-1)
    return array
};


CREATE OR REPLACE FUNCTION extract_endpoint(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    array = []
    for i in x:
        match = re.search(r'^.*"\S+ (\S+)\s*\S*\s*"', i)
        if match:
            array.append(match[1])
        else:
            array.append('')
    return array
};


CREATE OR REPLACE FUNCTION extract_ip(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    return [re.search(r"(^\S+) ", i)[1] for i in x]
};


CREATE OR REPLACE FUNCTION extract_protocol(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    return [re.search(r'^.*"(\S+) \S+\s*\S*\s*"', i)[1] for i in x]
};


CREATE OR REPLACE FUNCTION extract_method(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    return [re.search(r'^.*"\S+ \S+\s*(\S*)\s*"', i)[1] for i in x]
};


CREATE OR REPLACE FUNCTION extract_response_code(x varchar(256)) RETURNS INTEGER LANGUAGE PYTHON {
    import re
    array = []
    for i in x:
        match = re.search(r'^.*" (\d{3}) ', i)
        if match:
            array.append(int(match[1]))
        else:
            array.append(-1)
    return array
};


CREATE OR REPLACE FUNCTION extract_user_id(x varchar(256)) RETURNS varchar(256) LANGUAGE PYTHON {
    import re
    return [re.search(r"^\S+ \S+ (\S+) ", i)[1] for i in x]
};


SELECT ip, logDate, logMethod, endpoint, protocol, response_code, content_size
FROM (
        SELECT extract_ip(c1) as ip, extract_client_id(c1) as client_id,
               extract_user_id(c1) as user_id, extract_date(c1) as logDate,
               extract_method(c1) as logMethod, extract_endpoint(c1) as endpoint,
               extract_protocol(c1) as protocol, extract_response_code(c1) as response_code,
               extract_content_size(c1) as content_size
        FROM "weblogs"
        WHERE extract_endpoint(c1) <> ''
    ) as df
JOIN ip_blacklist as bad_ip_df ON df.ip = bad_ip_df."BadIPs";