docker pull bitnami/postgresql
docker run -d --name flask-postgres -e POSTGRESQL_USERNAME=myuser -e POSTGRESQL_PASSWORD=mypassword -e POSTGRESQL_DATABASE=mydatabase -p 5432:5432 bitnami/postgresql

### PgAdmin

docker pull dpage/pgadmin4
docker run -d -p 5050:80 --name pgadmin -e PGADMIN_DEFAULT_EMAIL=admin@email.com -e PGADMIN_DEFAULT_PASSWORD=password dpage/pgadmin4
http://localhost:5050

> to connect to dockerized db, use host.docker.internal for hostname instead of localhost
