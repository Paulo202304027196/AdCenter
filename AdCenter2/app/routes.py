from app.models import usuario
#from app.models import anuncio
#from app.models import contabilidade
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def init_app(app):
        
    #@app.route("/")
    #def principal():        
        #return render_template("seu_job/index.html")
    
    @app.route("/")
    def inicio():        
        return render_template("inicio.html")
    
    @app.route("/anuncio")
    def anuncio():
        return render_template("anuncio.html") #, anuncios=db.session(db.select(anuncio).order_by(anuncio.id)).scalars())
    
    
    @app.route("/admin")
    def admin():
        return render_template("admin.html")
            
    @app.route("/cad_user")
    def cad_user():        
        return render_template("cad_user.html")
    
    @app.route("/cad_anuncio")
    def cad_anuncio():
        return render_template("cad_anuncio.html")
    
    @app.route("/cad_admin")
    def cad_admin():
        return render_template("cad_admin.html")
    
    @app.route("/atualiza_user")
    def atualiza_user():        
        return render_template("atualiza_user.html")
    
    @app.route("/autaliza_anuncio/<int:id>", methods=["GET","POST"])
    def autaliza_anuncio():
        anuncio01=anuncios.query.filter_by(id=id).first()
        if request.method == "POST":
            título_anuncio = request.form["titulo_anuncio"]
            preço_anuncio = request.form["preço_anuncio"]
            link_anuncio = request.form["link_anuncio"]
            
            
            flash("Anúncio Atualizado Com Sucesso!")
            anuncio01.query.filter_by(id=id).update({"titulo_anuncios":titulo1})
            db.session.commit()
            return redirect(url_for("anuncio"))
        return render_template("atualiza_anuncio.html")

    #@app.route("/cadastro_anuncio", methods=["GET","POST"])
    #def cad_anuncio():
       # if request.method == "POST":
            #anun = anuncio()
           ## anun.titulo = request_form["titulo"]
           # db.session.add(anun)
           # db.session.commit()

          #  flash("Anúncio Criado Com Sucesso!")
           # return redirect(url_for("cad_anuncio"))
       # return render_template("cad_anuncio.html") 
