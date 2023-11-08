from app import db
from sqlalchemy import ForeignKey

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    correo = db.Column(db.String(100), nullable=False)
    clave_hash = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, unique=False)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,
                   primary_key=True)
    
    titulo = db.Column(db.String(100),
                       nullable=False)
    
    contenido = db.Column(db.String(500),
                          nullable=False)
    
    fecha_creacion = db.Column(db.Date,
                               nullable=False)
    
    autor_id = db.Column(db.Integer, 
                         ForeignKey('usuario.id'), 
                         nullable=False)
    
    categoria_id = db.Column(db.Integer, 
                             ForeignKey('categoria.id'), 
                             nullable=False)
    
    autor = db.relationship('Usuario')    

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id = db.Column(db.Integer,
                   primary_key=True)
    
    texto_comentario = db.Column(db.String(100), 
                                 nullable=False)
    
    fecha_creacion = db.Column(db.Date, 
                               nullable=False)
    
    autor_id = db.Column(db.Integer, 
                         ForeignKey('usuario.id'), 
                         nullable=False)
    
    post_id = db.Column(db.Integer, 
                        ForeignKey('post.id'), 
                        nullable=False)

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)
    