from flask import Flask, render_template               
app = Flask(__name__)                      

@app.route('/') 
def main():
   return render_template("index.html", rows=8, columns=8)

@app.route("/<int:rows>") 
def onlyRows(rows):
   return render_template("index.html", rows=rows, columns=8)

@app.route('/<int:rows>/<int:columns>') 
def rowsandcolumns(rows, columns):
   return render_template("index.html", rows=rows, columns=columns)


if __name__=="__main__":                      
   app.run(debug=True) 