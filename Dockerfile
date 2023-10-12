# Базовый образ — Python 3.9
FROM python:3.9

# Рабочий каталог
WORKDIR /app

# Копирование файла окружения в контейнер
COPY requirements.txt requirements.txt

# Установка окружения
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копирование кода модели и приложения в контейнер
COPY ["main.py","base_index.pkl","idx_hnsw.bin","mcbc_model.cbm","standard_scaler.pkl","Dockerfile","requirements.txt","./"] .

# Запуск приложения с помощью Gunicorn
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8989", "main:app"]