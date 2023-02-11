CREATE OR REPLACE FUNCTION fix_zip_codes(x varchar(20)) RETURNS varchar(20) LANGUAGE PYTHON {
    import string
    array = []
    for zips in x:
        if not zips:
            array.append("None")

        s = zips[:5]

        if s == "00000":
            array.append("None")
        else:
            array.append(s)
    return array
};


SELECT DISTINCT fix_zip_codes("Incident_Zip") AS Incident_Zip FROM "311";