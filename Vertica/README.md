# Vertica

## Create python udfs in vertica

Run the first command to create the library and then the second command for every function in the library. 


```
VerticaDB=> CREATE OR REPLACE LIBRARY libraryName AS '/path/to/lib.py' LANGUAGE 'Python';
VerticaDB=> CREATE OR REPLACE FUNCTION functionName AS LANGUAGE 'Python' NAME 'functionName_factory' LIBRARY libraryName fenced; 
```
