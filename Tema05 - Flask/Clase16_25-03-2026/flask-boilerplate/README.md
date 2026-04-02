# Flask Boilerplate

Este es un boilerplate de flask con algunas dependencias y configuraciones que se pueden usar para comenzar a desarrollar una aplicación Flask.

## Tecnologías y Requisitos

* **Python**: >= 3.12
* **Framework**: Flask 3.x
* **Base de datos**: PostgreSQL
* **Gestión de entorno**: venv

## Instalación y Configuración


1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/user/repo.git
    ```

2. **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    # En Linux/macOS
    source venv/bin/activate
    # En Windows
    venv\Scripts\activate
    ```

3. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Variables de entorno:** `.env`
    ```bash
    DATABASE_URI=''
    JWT_SECRET_KEY=''
    ```

## Migraciones

```bash
flask db init # Crea la carpeta migrations - Solo la primera vez
flask db migrate -m "Descripción de la migración" # Crea la migración
flask db upgrade # Actualiza la base de datos
```

## Ejecución

```bash
python run.py
```

## Estructura del proyecto

```bash
├── app
│   ├── models
│   │   ├── auth_model.py
│   │   ├── role_model.py
│   │   └── user_model.py
│   ├── resources
│   │   ├── auth_resource.py
│   │   ├── role_resource.py
│   │   └── user_resource.py
│   ├── schemas
│   │   ├── auth_schema.py
│   │   ├── role_schema.py
│   │   └── user_schema.py
│   └── services
│       ├── auth_service.py
│       ├── role_service.py
│       └── user_service.py
├── config.py
├── db.py
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   ├── versions
│   │   └── e1a0b3f0e0f3_.py
│   └── versions
│       └── e1a0b3f0e0f3_.py
├── README.md
├── requirements.txt
├── run.py
└── tests
    ├── test_auth_resource.py
    ├── test_role_resource.py
    └── test_user_resource.py
```

## Testing

```bash
pytest
```

## Despliegue
