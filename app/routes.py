from app.models import usuario
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
    
    @app.route("/user")
    def user():        
        return render_template("user.html")
    
    @app.route("/cad_user")
    def cad_user():        
        return render_template("cad_user.html")
    
    @app.route("/update_user")
    def update_user():        
        return render_template("update_user.html")
    
    @app.route("/ad")
    def ad():        
        return render_template("ad.html")
    
    @app.route("/cad_ad")
    def cad_ad():        
        return render_template("cad_ad.html")
    
    @app.route("/update_ad")
    def update_ad():        
        return render_template("update_ad.html")
    
    
    