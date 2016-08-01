echo 'America/Lima' > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
echo "timezone = 'America/Lima'" >> /var/lib/postgresql/data/postgresql.conf
