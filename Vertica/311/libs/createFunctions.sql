-- CREATE LIBRARY
CREATE OR REPLACE LIBRARY _311lib AS '/home/dbadmin/vertica_libs/311Vertica.py' LANGUAGE 'Python';

-- CREATE FUNCTIONS
CREATE OR REPLACE FUNCTION fix_zip_codes AS LANGUAGE 'Python' NAME 'fix_zip_codes_factory' LIBRARY _311lib fenced;