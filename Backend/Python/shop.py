from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/cart")
def cart():
    # read category - Request: I use Request to read the category from the URL
    category = request.args.get("category") # looks for the parameter "categorys"
    return render_template("cart.html")

# Function to generate the category bar at the top of the page
@app.route("/category_bar")
def category_bar():
    # temporary - future: will be filled dynamically out of the DB
    categorys = ["category A", "category B", "category C", "category D", "category E", "category F", "category G", "category H", "category I", "category J", "category K", "category L"]
    # generating html-code
    html = ""
    for c in categorys:
        link = f"/cart?category={c}" # creating a link to reach the page for the category-overview
        html += f"""
          <div class="entry"><a href="{link}">{c}</div> 
        """
    # returning generated code
    return html

@app.route("/products")
def products():
    produkte = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    html = """
<title>Slideshow Galerie</title>

<div class="gallery-container">
  <div class="gallery-slider">

    """
    for i in range(0, len(produkte), 4): # 4 products per slide
      html += '<div class="slide-group">\n'
      for p in produkte[i:i+4]: # get the next 4 products
          html += f"""
          <div class="gallery-item">
            <!-- <img src="{p}.jpg" alt="Bild {p}"> -->
            <img src="{ url_for('static', filename='res/placeholder.png') }" alt="Placeholder für Produkt {p}">
            <div class="caption">Überschrift {p}</div>
          </div>
          """
      html += '</div>\n'
    
    html += """
  </div>
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
    """
# &#10094; -> left arrow
# &#10095; -> right arrow

    return html  # Returns raw HTML

@app.route("/bottomBar")
def bottom_bar():
    return """
    <div class="bottom_bar">
        <p>© 2025 Was-wird-shop | Impressum | Datenschutz</p>
    </div>
    """

if __name__ == "__main__":
    app.run(debug=True)