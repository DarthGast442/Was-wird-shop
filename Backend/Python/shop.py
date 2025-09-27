from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/produkte")
def produkte():
    produkte = ["Apfel", "Banane", "Orange"]
    html = ""
    for p in produkte:
        html += f"<div class='produkt-item'>{p}</div>"
    return html  # Liefert reines HTML zurück

if __name__ == "__main__":
    app.run(debug=True)