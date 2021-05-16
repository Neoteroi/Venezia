# Alembic

This application uses `Alembic` to handle database migrations. However, it does
not use the ORM solution provided in `SQLAlchemy`.

References:
[See the documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).
[SQLAlchemy 1.4 / 2.0 Tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html).

## Quick reference

```bash
# create a new revision
alembic revision -m "create nodes table"

# review and configure the migration as desired...

# apply a migration using the CLI (requires connection string configured in alembic.ini)
alembic upgrade head

# see history
alembic history --verbose

alembic current
```

To revert to the beginning:

```bash
alembic downgrade base
```
