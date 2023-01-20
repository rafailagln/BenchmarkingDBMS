CREATE TABLE "weblogs_2" (
    "c1" varchar(500)
);

INSERT INTO "weblogs_2" ("c1") SELECT "c1" FROM "weblogs";
INSERT INTO "weblogs_2" ("c1") SELECT "c1" FROM "weblogs";

CREATE TABLE "weblogs_4" (
    "c1" varchar(500)
);

INSERT INTO "weblogs_4" ("c1") SELECT "c1" FROM "weblogs_2";
INSERT INTO "weblogs_4" ("c1") SELECT "c1" FROM "weblogs_2";

CREATE TABLE "weblogs_8" (
    "c1" varchar(500)
);

INSERT INTO "weblogs_8" ("c1") SELECT "c1" FROM "weblogs_4";
INSERT INTO "weblogs_8" ("c1") SELECT "c1" FROM "weblogs_4";

CREATE TABLE "weblogs_16" (
    "c1" varchar(500)
);

INSERT INTO "weblogs_16" ("c1") SELECT "c1" FROM "weblogs_8";
INSERT INTO "weblogs_16" ("c1") SELECT "c1" FROM "weblogs_8";

CREATE TABLE "weblogs_32" (
    "c1" varchar(500)
);

INSERT INTO "weblogs_32" ("c1") SELECT "c1" FROM "weblogs_16";
INSERT INTO "weblogs_32" ("c1") SELECT "c1" FROM "weblogs_16";



SELECT COUNT(*) FROM "weblogs";
SELECT COUNT(*) FROM "weblogs_2";
SELECT COUNT(*) FROM "weblogs_4";
SELECT COUNT(*) FROM "weblogs_8";
SELECT COUNT(*) FROM "weblogs_16";
SELECT COUNT(*) FROM "weblogs_32";