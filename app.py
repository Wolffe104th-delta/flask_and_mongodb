from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

# Tworzymy instancję aplikacji Flask
app = Flask(__name__)

# Inicjalizujemy klient MongoDB - łączymy się z kontenerem 'mongo'
client = MongoClient("mongodb://mongo:27017/")

# Tworzymy bazę 'blog' i kolekcję 'posts'
db = client["blog"]
posts_collection = db["posts"]

# Endpoint: strona główna, pokazuje wszystie posty
@app.route('/')
def index():
    try:
        posts = list(posts_collection.find()) # Pobieramy dane z Mongo
    except Exception as e:
        return f"<h1>Mongo error</h1><pre>{e}</pre>"
    return render_template('index.html', posts=posts) # Przekazujemy do szablonu

# Endpoint: Formularz dodawania nowego posta
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        # Tworzymy słownik z danymi z formularza
        post = {
            "title": request.form['title'],
            "content": request.form['content']
        }
        posts_collection.insert_one(post) # Zapisuje do Mongo
        return redirect('/') # Po zapisie wracamy na stronę główną
    return render_template('new_post.html') # GET: pokaż formularz

# Uruchamiamy aplikację Flask (nasłuchujemy na porcie 5000) 
if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
