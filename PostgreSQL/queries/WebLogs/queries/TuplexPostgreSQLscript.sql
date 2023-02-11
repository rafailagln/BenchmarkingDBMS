create or replace function extract_client_id(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r"^\S+ (\S+) ", x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_client_id(varchar) owner to postgres;



create or replace function extract_content_size(x character varying) returns integer
    language plpython3u
as
$$
import re

match = re.search(r'^.*" \d{3} (\S+)', x)
if match:
    return 0 if match[1] == '-' else int(match[1])
else:
    return -1
$$;

alter function extract_content_size(varchar) owner to postgres;



create or replace function extract_date(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r"^.*\[([\w:/]+\s[+\-]\d{4})\]", x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_date(varchar) owner to postgres;



create or replace function extract_endpoint(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r'^.*"\S+ (\S+)\s*\S*\s*"', x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_endpoint(varchar) owner to postgres;



create or replace function extract_ip(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r"(^\S+) ", x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_ip(varchar) owner to postgres;



create or replace function extract_method(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r'^.*"(\S+) \S+\s*\S*\s*"', x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_method(varchar) owner to postgres;



create or replace function extract_protocol(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r'^.*"\S+ \S+\s*(\S*)\s*"', x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_protocol(varchar) owner to postgres;



create or replace function extract_response_code(x character varying) returns integer
    language plpython3u
as
$$
import re

match = re.search(r'^.*" (\d{3}) ', x)
if match:
    return int(match[1])
else:
    return -1
$$;

alter function extract_response_code(varchar) owner to postgres;



create or replace function extract_user_id(x character varying) returns text
    language plpython3u
as
$$
import re

match = re.search(r"^\S+ \S+ (\S+) ", x)
if match:
    return match[1]
else:
    return ''
$$;

alter function extract_user_id(varchar) owner to postgres;



create or replace function randomize_udf(x character varying) returns text
    language plpython3u
as
$$
import re
import random
return re.sub('^/~[^/]+', '/~' + ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for t in range(10)]), x)
$$;

alter function randomize_udf(varchar) owner to postgres;



SELECT ip, date, method, endpoint, protocol, response_code, content_size
FROM (
        SELECT extract_ip(c1) as ip, extract_client_id(c1) as client_id,
               extract_user_id(c1) as user_id, extract_date(c1) as date,
               extract_method(c1) as method, extract_endpoint(c1) as endpoint,
               extract_protocol(c1) as protocol, extract_response_code(c1) as response_code,
               extract_content_size(c1) as content_size
        FROM "weblogs"
        WHERE extract_endpoint(c1) != ''
    ) as df
JOIN ip_blacklist as bad_ip_df ON df.ip = bad_ip_df."BadIPs";