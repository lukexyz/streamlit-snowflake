# streamlit-snowflake
❄️ Intro to snowflake cloud databases

## 1. Snowflake Console
`docs.streamlit.io` [Tutorial](https://docs.streamlit.io/knowledge-base/tutorials/databases/snowflake#create-a-snowflake-database)

Run the following in the snowflake console.
```sql
CREATE DATABASE PETS;

CREATE TABLE MYTABLE (
    NAME            varchar(80),
    PET             varchar(80)
);

INSERT INTO MYTABLE VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');

SELECT * FROM MYTABLE;
```

## 2. Secrets
* Put in `.streamlit/secrets.toml`
```toml
[snowflake]
user = "xxx"
password = "xxx"
account = "xxx"
warehouse = "COMPUTE_WH"
database = "PETS"
schema = "PUBLIC"
```