FROM postgres
MAINTAINER cyacarini@rcp.pe

FROM library/postgres
ADD init.sql /docker-entrypoint-initdb.d/
ADD set_locale.sh /docker-entrypoint-initdb.d/
