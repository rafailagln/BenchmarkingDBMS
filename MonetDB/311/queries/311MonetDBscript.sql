CREATE OR REPLACE FUNCTION fix_zip_codes(x STRING) RETURNS STRING LANGUAGE PYTHON {
    import string
    array = []
    for zips in x:
        if not zips:
            array.append(None)

        s = zips[:5]

        if s == "00000":
            array.append(None)
        else:
            array.append(s)
    return array
};


SELECT DISTINCT sys.fix_zip_codes("Incident Zip") AS Incident_Zip FROM sys."311";