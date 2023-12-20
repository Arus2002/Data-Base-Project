DB_NAME="my_project"
DB_USER="arusyak"
DB_PASSWORD="pass123"
DB_OWNER="arusyak"

sudo -u postgres createdb $DB_NAME

sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"

sudo -u postgres psql -c "ALTER DATABASE $DB_NAME OWNER TO $DB_OWNER;"
