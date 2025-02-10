# FastAPI API Project

Este proyecto es una API desarrollada con FastAPI y Python.

## Requisitos previos

Asegúrate de tener instalados los siguientes requisitos antes de comenzar:

- Python 3.8 o superior
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (para ejecutar el servidor ASGI)

## Instalación

1. Clona este repositorio:
   ```sh
   git clone git@github.com:JesusAraujoDEV/LenguajesDePrograma.git
   cd '.\LenguajesDePrograma\Actividad 3\FastAPI\'  
   ```
2. Crea un entorno virtual y actívalo:
   ```sh
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En macOS/Linux
   source venv/bin/activate
   ```
3. Instala las dependencias necesarias:
   ```sh
   pip install -r requirements.txt
   ```

## Ejecución del servidor

Ejecuta el servidor de desarrollo con Uvicorn:
```sh
fastapi dev
```

La API estará disponible en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Documentación automática

FastAPI genera documentación automáticamente:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Variables de entorno

Crea un archivo `.env` para almacenar variables sensibles como claves secretas, credenciales de base de datos, etc.

Ejemplo:
```
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
SECRET_KEY=mysecretkey
```

## Pruebas

Para ejecutar las pruebas, usa:
```sh
pytest tests/
```

## Despliegue

Para producción, se recomienda ejecutar Uvicorn con Gunicorn:
```sh
gunicorn -k uvicorn.workers.UvicornWorker main:app
```

También puedes desplegar en servicios como:
- Docker
- Heroku
- AWS, GCP, Azure

## Contribuciones

Si deseas contribuir, por favor abre un **Issue** o un **Pull Request**.

## Licencia

Este proyecto está bajo la licencia MIT.

