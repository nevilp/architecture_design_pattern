#!/bin/bash
echo "wal_level = replica" >> /var/lib/postgresql/data/postgresql.conf
echo "max_wal_senders = 10" >> /var/lib/postgresql/data/postgresql.conf
echo "hot_standby = on" >> /var/lib/postgresql/data/postgresql.conf
echo "host replication replica 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf