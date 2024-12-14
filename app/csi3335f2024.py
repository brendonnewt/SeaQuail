import os

mysql = {
    "host": os.getenv("MYSQL_HOST", "db:3307"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "password"),
    "db": os.getenv("MYSQL_DATABASE", "seaquail"),
}
