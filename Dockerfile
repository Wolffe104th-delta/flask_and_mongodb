# Używamy oficjalnego lekkiego obrazu Python
FROM python:3.10-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik z zależnościami i instalujemy pakiety
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiujemy resztę plików (aplikacja, szablony itp.)
COPY . .

# Otwieramy port 5000 dla Flask
EXPOSE 5000 

# Uruchamiamy aplikację
CMD ["python", "-u", "app.py"] 
