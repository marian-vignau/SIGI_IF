alembic revision --autogenerate -m "new db version"

@echo created automigration
@echo now, run: >>> alembic upgrade head