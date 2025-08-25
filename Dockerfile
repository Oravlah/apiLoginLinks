# Usamos imagen oficial de Python ligera
FROM python:3.12-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiamos todo el código del proyecto
COPY . .

# Exponemos el puerto donde Django servirá la API
EXPOSE 8000

# Comando para correr la API con Gunicorn
CMD ["gunicorn", "projectprinc.wsgi:application", "--bind", "0.0.0.0:8000"]
