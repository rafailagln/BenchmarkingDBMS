create table if not exists ip_blacklist_2
(
    "BadIPs" varchar(100)
);

INSERT INTO "ip_blacklist_2" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist";
INSERT INTO "ip_blacklist_2" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist";

create table if not exists ip_blacklist_4
(
    "BadIPs" varchar(100)
);

INSERT INTO "ip_blacklist_4" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_2";
INSERT INTO "ip_blacklist_4" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_2";

create table if not exists ip_blacklist_8
(
    "BadIPs" varchar(100)
);

INSERT INTO "ip_blacklist_8" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_4";
INSERT INTO "ip_blacklist_8" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_4";

create table if not exists ip_blacklist_16
(
    "BadIPs" varchar(100)
);

INSERT INTO "ip_blacklist_16" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_8";
INSERT INTO "ip_blacklist_16" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_8";

create table if not exists ip_blacklist_32
(
    "BadIPs" varchar(100)
);

INSERT INTO "ip_blacklist_32" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_16";
INSERT INTO "ip_blacklist_32" ("BadIPs") SELECT "BadIPs" FROM "ip_blacklist_16";

SELECT COUNT(*) FROM "ip_blacklist";
SELECT COUNT(*) FROM "ip_blacklist_2";
SELECT COUNT(*) FROM "ip_blacklist_4";
SELECT COUNT(*) FROM "ip_blacklist_8";
SELECT COUNT(*) FROM "ip_blacklist_16";
SELECT COUNT(*) FROM "ip_blacklist_32";