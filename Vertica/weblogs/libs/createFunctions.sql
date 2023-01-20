-- CREATE LIBRARY
CREATE OR REPLACE LIBRARY weblogslib AS '/home/dbadmin/vertica_libs/weblogsVertica.py' LANGUAGE 'Python';

-- CREATE FUNCTIONS
CREATE OR REPLACE FUNCTION extract_ip AS LANGUAGE 'Python' NAME 'extract_ip_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_client_id AS LANGUAGE 'Python' NAME 'extract_client_id_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_user_id AS LANGUAGE 'Python' NAME 'extract_user_id_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_date AS LANGUAGE 'Python' NAME 'extract_date_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_method AS LANGUAGE 'Python' NAME 'extract_method_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_endpoint AS LANGUAGE 'Python' NAME 'extract_endpoint_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_protocol AS LANGUAGE 'Python' NAME 'extract_protocol_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_response_code AS LANGUAGE 'Python' NAME 'extract_response_code_factory' LIBRARY weblogslib fenced;
CREATE OR REPLACE FUNCTION extract_content_size AS LANGUAGE 'Python' NAME 'extract_content_size_factory' LIBRARY weblogslib fenced;