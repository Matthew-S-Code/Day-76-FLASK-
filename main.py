from flask import Flask
import datetime

today = datetime.date.today()

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
  page = f"""<html>
  <head>
  <title>Landing page</title>
  <h1>landing page</h1>
  </head>
  <body>
  <p><a href = "/portfolio">Go to portfolio</a></p>
  <p><a href="/linkTree">Go to link tree</a></p>
  <p>Todays date: {today}</p>
  </body>
  </html>"""
  return page

@app.route("/portfolio")
def portfolio():
  page = """<html>
  <head>
    <title>Portfolio</title>
    <link href="static/css/port.css" rel="stylesheet" type="text/css" />
  </head>
<body>
<div>
<h1>Matthew's Portfolio</h1>
</div>
  <div>
  <h2>Rock Paper Scissors</h2>
  <a href="https://github.com/Matthew-S-Code/Day-17-Replit100DaysOfCode-"><img src="static/imagesLinkt/imagesPort/rockpaperscissors.jpg" width = "20%" height = "20%"></a>
  <p>I made a working rock paper scissors game</p>
  </div>

  <div>
<h2>Hangman</h2>
  <a href="https://github.com/Matthew-S-Code/Day-39-Replit100DaysOfCode"><img src = "static/imagesLinkt/imagesPort/hangman.jpg" width = "20%" height = "20%" class="hangman"></a>
  <p>I made a working hangman game</p>
  </div>

  <div>
<h2>Pizza ordering system</h2>
  <a href="https://github.com/Matthew-S-Code/Day-52-Pizza-Ordering-System"><img src="static/imagesLinkt/imagesPort/pizza.jpg" width = "20%" height = "20%" class="pizza"></a>
  <p>I made a pizza ordering system</p>
  </div>

  <div>
<h2>Visual Novel</h2>
  <a href="https://github.com/Matthew-S-Code/Day-69-Visual-Novel"><img src="static/imagesLinkt/imagesPort/tkinter.png" width="20%" height="20%"></a>
  <p>I made a visual novel with a user interface using the tkinter python library</p>
  </div>

  <div>
  <h2>Hashing and salting</h2>
  <a href="https://github.com/Matthew-S-Code/Day-71-hashing-and-salting-"><img src="static/imagesLinkt/imagesPort/hashSalt.png" width="20%" height="20%"></a>
  <p>I learned hashing and salting for passwords</p>
  </div>


  <a href="https://www.w3schools.com/css/default.asp"><p class="css">W3Schools css</p></a>

  <p><a href = "/">Go to landing page</a></p>
</body>
</html>"""
  return page

@app.route("/linkTree")
def linkTree():
  page = """<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Link Tree</title>
  <link href="static/css/style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <div>
    <h1>Link Tree</h1>
  </div>
  <div>
    <img src="static/imagesLinkt/BUCS-63.jpg" width="20%" height="20%">
  </div>
  <div>
    <p class="here">Here are my socials:</p>
    <p>
      <a href="https://github.com/Matthew-S-Code">Github</a><br>
      <a href="https://www.linkedin.com/in/matthew-saldanha-392804216/">LinkedIn</a><br>
      <a href="https://www.instagram.com/matt_saldanha2702/">Instagram </a>
    </p>
  </div>
  

  <p><a href = "/">Go to landing page</a></p>
  <script src="script.js"></script>

</body>

</html>"""
  return page


app.run(host='0.0.0.0', port=81)
