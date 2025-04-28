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
1. Click on the security group id
1. `Edit inbound rules`
1. Delete the group rule, and add a new one with the following parameters:
    -  `Type`: `PostgreSQL` (or other database)
    - `Source`: `MyIP`
    - `Description`: Add helpful description

1. Download the CA certificate bundle that matches your RDS instance region listed in the `Security` tab of the database [see docs here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.RegionCertificates) and add to project
1. Configure the database connection to enable SSL and point to the path to that CA
    ```
    dbConfig = {
        ...
        ssl: { 
            require: true,
            rejectUnauthorized: true,
            ca: fs.readFileSync('/pathto/rds-ca-cert.pem').toString(), 
        }
    } 
    ```