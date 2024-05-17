from app.models import usuario
from app.models import anuncios
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
    
    
    @app.route("/", methods=["GET", "POST"])
    def index():
        form = LoginForm()
        
        if form.validate_on_submit():
            user = usuario.query.filter_by(email=form.email.data).first()

            if not user:
                flash("Email Incorreto, verifique!")
                return redirect(url_for("index"))
            
            elif not check_password_hash(user.senha, form.senha.data):
                flash("Senha Incorreta, verifique!")
                return redirect(url_for("index"))
            
            login_user(user, remember=form.remember.data, duration=timedelta(days=7))
            return redirect(url_for("inicio"))
        
        return render_template("index.html", form=form)

    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("index"))

    @app.route("/inicio")
    def inicio():        
        return render_template("inicio.html")
    
    @app.route("/anuncio")
    def anuncio():
        return render_template("anuncio.html", anuncio=db.session.execute(db.select(anuncios).order_by(anuncios.id)).scalars())
    
    @app.route("/excluir/<int:id>")
    def excluir_anun(id):
        delete=anuncios.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for("anuncio"))

    @app.route("/cad_anuncio", methods=["GET", "POST"])
    def cad_anuncio():        
        if request.method == "POST":
            ad = anuncios()
            ad.titulo = request.form["titulo"]
            ad.preco = request.form["preco"]
            ad.links = request.form["links"]
            ad.plataforma = request.form["plataforma"]
            db.session.add(ad)
            db.session.commit()
                            
            flash("Anúncio criado com sucesso!")       
            return redirect(url_for("cad_anuncio"))
        return render_template("cad_anuncio.html")

    @app.route("/atualiza_anuncio/<int:id>", methods=["GET", "POST"])
    def atualiza_anuncio():
        ads = anuncios.query.filter_by(id=id).first()        
        if request.method == "POST":
            
                            
            flash("Anúncio criado com sucesso!")       
            return redirect(url_for("cad_anuncio"))
        return render_template("cad_anuncio.html")
        
    @app.route("/admin")
    def admin():
        return render_template("admin.html")
            
    @app.route("/cad_user", methods=["GET", "POST"])
    def cad_user():        
        if request.method == "POST":
            user = usuario()
            user.email = request.form["email"]
            user.nome = request.form["nome"]        
            user.senha = generate_password_hash(request.form["senha"])
            db.session.add(user)
            db.session.commit()
                            
            flash("Usuario criado com sucesso!")       
            return redirect(url_for("cad_user"))
        return render_template("cad_user.html")
    
    @app.route("/cad_admin")
    def cad_admin():
        return render_template("cad_admin.html")
    
    @app.route("/atualiza_user")
    def atualiza_user():        
        return render_template("atualiza_user.html")
    

    