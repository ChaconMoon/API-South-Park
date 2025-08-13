FROM python:3.13-slim

# Configurar variables de entorno para Poetry
ENV POETRY_NO_INTERACTION=1 \
        POETRY_VENV_IN_PROJECT=1 \
        POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Instalar Poetry
RUN pip install poetry

# Copiar código
COPY . .
# Instalar dependencias con Poetry
RUN poetry install

EXPOSE 8000

# Ejecutar con Poetry
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]