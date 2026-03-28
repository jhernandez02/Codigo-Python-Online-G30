# Flask Boilerplate

## Instalación

```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-restful
pip install pydantic
pip install psycopg2-binary
pip install flask-cors
pip install flask-jwt-extended
pip install python-dotenv
pip install flask-migrate
pip install bcrypt
```

```bash
pip install -r requirements.txt
```

## Migraciones

```bash
flask db init # Crea la carpeta migrations - Solo la primera vez
flask db migrate -m "Descripción de la migración" # Crea la migración
flask db upgrade # Actualiza la base de datos
```