from flask import Flask, render_template, request

app = Flask(__name__)

cities_list = ["Göteborg", "Linköping", "Enköping", "Skövde", "Mölndal"]

#render_template letar efter html filer i /templates mappen.
@app.route("/")
def index():
    return render_template("index.html", title="Kristians hemsida", show_paragraph=True, cities=cities_list) #Jag kan skicka med olika typer av variabler i min render_template
# det är render_template() som ser till att variablerna renderas in i html. Den kör igenom logiken och returnerar korrekt html.  

@app.route("/submit", methods=["POST"])
def submit():
    print(request.form["email"]) #Data från formulär kommer du åt via request.form
    return "Tack formuläret har skickats in!"

"""
1. render_template(). Vilken mapp letar den i?
2. variabler i template {{variable}}
3. if-statements {% if condition %}
4. for loops {% for item in list %}
5. formulär
"""