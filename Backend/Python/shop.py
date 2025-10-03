from flask import Flask, render_template, request

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
  <div class="gallery-slider" id="slider">

    """
    for p in produkte:
        html += f"""
    <div class="gallery-item">
      <img src="{p}.jpg" alt="Bild {p}">
      <div class="caption">Überschrift {p}</div>
    </div>
    """
    
    html += """
  </div>
  <a class="prev" onclick="plusSlides(-1, 0)">&#10094;</a>
  <a class="next" onclick="plusSlides(1, 0)">&#10095;</a>
</div>

<script>
let slideIndex = [1,1];
let slideId = ["mySlides1", "mySlides2"]
showSlides(1, 0);
showSlides(1, 1);

function plusSlides(n, no) {
  showSlides(slideIndex[no] += n, no);
}

function showSlides(n, no) {
  let i;
  let x = document.getElementsByClassName(slideId[no]);
  if (n > x.length) {slideIndex[no] = 1}    
  if (n < 1) {slideIndex[no] = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  x[slideIndex[no]-1].style.display = "block";  
}
</script>
    """
    
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