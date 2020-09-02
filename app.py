from flask import Flask, render_template,url_for, request, redirect

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template("Strona_Kubicy.html")

@app.route('/mypage/contact')
def contact():
    return render_template("Strona_Kubicy1.html")

@app.route('/mypage/contact', methods= ['POST', 'GET'])
def message():
    if request.method == 'GET':
        return render_template("Strona_Kubicy1.html")
    elif request.method == 'POST':
        print (request.form)
        return redirect('/mypage/contact')
    
