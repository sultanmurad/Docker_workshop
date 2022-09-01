FROM postgres:latest
ENV POSTGRES_DB=YaDB
ENV POSTGRES_USER=YaUser
ENV POSTGRES_PASSWORD=YaPassword
COPY init_db.sql /docker-entrypoint-initdb.d/init_db.sql
VOLUME data:/var/lib/postgresql/data

