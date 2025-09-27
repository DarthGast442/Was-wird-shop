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

if __name__ == "__main__":
    app.run(debug=True)