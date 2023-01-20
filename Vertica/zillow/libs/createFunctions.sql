-- CREATE LIBRARY
CREATE OR REPLACE LIBRARY zillowlib AS '/home/dbadmin/vertica_libs/zillowVertica.py' LANGUAGE 'Python';

-- CREATE FUNCTIONS
CREATE OR REPLACE FUNCTION extractprice_sell AS LANGUAGE 'Python' NAME 'extractprice_sell_factory' LIBRARY zillowlib fenced;
CREATE OR REPLACE FUNCTION extractsqfeet AS LANGUAGE 'Python' NAME 'extractsqfeet_factory' LIBRARY zillowlib fenced;
CREATE OR REPLACE FUNCTION extractba AS LANGUAGE 'Python' NAME 'extractba_factory' LIBRARY zillowlib fenced;
CREATE OR REPLACE FUNCTION extractbd AS LANGUAGE 'Python' NAME 'extractbd_factory' LIBRARY zillowlib fenced;
CREATE OR REPLACE FUNCTION extractpcode AS LANGUAGE 'Python' NAME 'extractpcode_factory' LIBRARY zillowlib fenced;
CREATE OR REPLACE FUNCTION extracttype AS LANGUAGE 'Python' NAME 'extracttype_factory' LIBRARY zillowlib fenced;
CREATE OR REPLACE FUNCTION extractid AS LANGUAGE 'Python' NAME 'extractid_factory' LIBRARY zillowlib fenced;