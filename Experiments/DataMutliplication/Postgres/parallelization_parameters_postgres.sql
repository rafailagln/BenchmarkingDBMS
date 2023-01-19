set max_parallel_workers_per_gather=1;
set max_parallel_workers=1;
set max_parallel_maintenance_workers=1;
select * from pg_settings where name like '%par%';
SELECT name, setting FROM pg_settings WHERE name = 'max_worker_processes'
                                        OR name = 'max_parallel_workers_per_gather'
                                        OR name = 'max_parallel_workers'
                                        OR name = 'max_parallel_maintenance_workers';
-- change at: /etc/postgresql/15/main/postgresql.conf
-- sudo systemctl restart postgresql.service