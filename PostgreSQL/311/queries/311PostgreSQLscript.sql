create function fix_zip_codes(zips character varying) returns text
    language plpython3u
as
$$
    if not zips:
        return None

    s = zips[:5]

    if s == "00000":
        return None
    else:
        return s
$$;

alter function fix_zip_codes(varchar) owner to postgres;


SELECT DISTINCT fix_zip_codes("Incident Zip") AS Incident_Zip FROM public."311";