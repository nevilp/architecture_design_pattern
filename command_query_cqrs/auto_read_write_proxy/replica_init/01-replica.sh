#!/bin/bash
set -e

# Wait for master to be ready
until pg_isready -h postgres-master -p 5432 -U postgres; do
  echo "Waiting for master..."
  sleep 2
done

# Stop PostgreSQL server
pg_ctl -D "$PGDATA" -m fast stop

# Clean old data
rm -rf "$PGDATA"/*

# Base backup from master
PGPASSWORD=postgres pg_basebackup -h postgres-master -U replica -D "$PGDATA" -Fp -Xs -P -R

# Adjust permissions
chown -R postgres:postgres "$PGDATA"
