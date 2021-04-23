from flask import Flask, render_template, redirect               
app = Flask(__name__)                      


@app.route('/')  
def index():  
   return redirect('/play')
@app.route('/play')
def play():  
   return render_template('index.html', times=3, color= 'blue')
@app.route('/play/<int:x>')
def num_play(x):  
   return render_template('index.html', times=x, color= 'blue')
@app.route('/play/<int:x>/<color>')
def color(x, color):
   return render_template('index.html', times=x, color=color)



if __name__=="__main__":                      
   app.run(debug=True) 