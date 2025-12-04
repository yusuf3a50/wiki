# postgreSQL

## Installation
sudo apt install postgresql

## Setup
```bash
systemctl status postgresql
systemctl enable postgresql
systemctl start postgresql
```
or use `service` if your system does not implement `systemd`

## User management

Check postgres user password status:
```bash
sudo passwd -S postgres
```

Create user:
```bash
sudo -u postgres createuser -P testuser
```

Connect as user:
```bash
psql -h localhost -p 5432 -U testuser -d postgres
```

Drop user:
```bash
sudo -u postgres dropuser testuser
```

## Database management

### Create a new database

As postgres superuser:
```bash
sudo -u postgres createdb mydb
# or with owner
sudo -u postgres createdb -O testuser mydb
```

From psql:
```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE mydb;
CREATE DATABASE mydb OWNER testuser;
-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE mydb TO testuser;
\q
```

### List databases
```bash
sudo -u postgres psql -c "\l"
# or in psql
\l
```

### Connect to database
```bash
psql -h localhost -p 5432 -U testuser -d mydb
# or if peer auth is configured
sudo -u postgres psql -d mydb
```

### Drop database
```bash
sudo -u postgres dropdb mydb
# or in psql
DROP DATABASE mydb;
```

### Switch database in psql
```sql
\c mydb
```