from app.models import usuario
from app.models import anuncio
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
            
    @app.route("/cad_user")
    def cad_user():        
        return render_template("cad_user.html")
    
    @app.route("/atualiza_user")
    def atualiza_user():        
        return render_template("atualiza_user.html")
    
    @app.route("/admin")
    def admin():        
        return render_template("admin.html")
    
    @app.route("/cad_admin")
    def cad_admin():      
        return render_template("cad_admin.html")
    
    @app.route("/atualiza_admin")
    def atualiza_admin():        
        return render_template("atualiza_admin.html")
    
    @app.route("/anuncio")
    def anuncio():        
        return render_template("anuncio.html", anuncios=db.session(db.select(anuncio).order_by(anuncio.id)).scalars())
    @app.route("/excluir_anuncio / < int:id > ")
    def excluir_anuncio():        
