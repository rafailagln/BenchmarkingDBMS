CREATE TABLE "311_2" (
    "Incident_Zip" varchar
);

INSERT INTO "311_2" ("Incident_Zip") SELECT "Incident_Zip" FROM "311";
INSERT INTO "311_2" ("Incident_Zip") SELECT "Incident_Zip" FROM "311";

CREATE TABLE "311_4" (
    "Incident_Zip" varchar
);

INSERT INTO "311_4" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_2";
INSERT INTO "311_4" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_2";

CREATE TABLE "311_8" (
    "Incident_Zip" varchar
);

INSERT INTO "311_8" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_4";
INSERT INTO "311_8" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_4";

CREATE TABLE "311_16" (
    "Incident_Zip" varchar
);

INSERT INTO "311_16" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_8";
INSERT INTO "311_16" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_8";

CREATE TABLE "311_32" (
    "Incident_Zip" varchar
);

INSERT INTO "311_32" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_16";
INSERT INTO "311_32" ("Incident_Zip") SELECT "Incident_Zip" FROM "311_16";


SELECT COUNT(*) FROM "311";
SELECT COUNT(*) FROM "311_2";
SELECT COUNT(*) FROM "311_4";
SELECT COUNT(*) FROM "311_8";
SELECT COUNT(*) FROM "311_16";
SELECT COUNT(*) FROM "311_32";