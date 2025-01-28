#!/bin/sh

superset db upgrade
echo "Created migrations"
superset fab create-admin --username $ADMIN_USERNAME --firstname $ADMIN_FIRSTNAME --lastname $ADMIN_LASTNAME --email $ADMIN_EMAIL --password $ADMIN_PASSWORD
echo "Created Admin user"
superset init
echo "Initialize Superset"

superset set-database-uri -u $SQLALCHEMY_DATABASE_URI -d dashboard
exec "$@"