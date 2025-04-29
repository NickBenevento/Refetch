# API

Uses:
- FastAPI + Pydantic
- SQLAlchemy (and SQLModel)
- Postgres


## Configuring AWS RDS Instance:

### Creating the database
1. Go to the [AWS databases page](https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#databases:)
2. Create a new database
    - Make sure to select `Yes` for `Public Access` in the `Connectivity` tab

### Editing configuration for connections
1. Click on the database once created, and click the `VPC security groups` in the `Security` tab
2. Click on the security group id
3. `Edit inbound rules`
4. Delete the group rule, and add a new one with the following parameters:
    -  `Type`: `PostgreSQL` (or other database)
    - `Source`: `MyIP`
    - `Description`: Add helpful description
5. Download the CA certificate bundle that matches your RDS instance region listed in the `Security` tab of the database [see docs here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificates) and add to project in `certs/` directory.
6. Install `pg8000` and pass in to the url drivername:
`drivername="postgresql+pg8000"`
7. Use Python `ssl` library to create a context:
```
pem_path = os.path.abspath("/path/to/.pem")
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.load_verify_locations(pem_path)
```
8. Create db args and pass it in as `connect_args`:
```
db_args = {"check_same_thread": False, "sslmode": "require", "ssl_context": ssl_context}

engine = create_engine(DATABASE_URL, connect_args={"ssl_context": ssl_context})
```