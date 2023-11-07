from app import db
from sqlalchemy import ForeignKey

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    clave = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return self.nombre
    

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

    def get_nombre(self):
        usuario = db.session.query(Usuario).filter_by(
                  id = self.autor_id
                  ).all()
        usuario_nombre = usuario[0].nombre
        return (
            usuario_nombre
    )
    
    def get_categoria(self):
        categoria = db.session.query(Categoria).filter_by(
                                    id = self.categoria_id
                                    ).all()
        
        nombre_categoria = categoria[0].categoria
        return (
            nombre_categoria
    )

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id = db.Column(db.Integer,
                   primary_key=True)
    
    texto_comentario = db.Column(db.String(500), 
                                 nullable=False)
    
    fecha_creacion = db.Column(db.String(100), 
                               nullable=False)
    
    autor_id = db.Column(db.Integer, 
                         ForeignKey('usuario.id'), 
                         nullable=False)
    
    post_id = db.Column(db.Integer, 
                        ForeignKey('post.id'), 
                        nullable=False)

    def get_nombre(self):
        usuario = db.session.query(Usuario).filter_by(
                  id = self.autor_id
                  ).all()
        usuario_nombre = usuario[0].nombre
        return (
            usuario_nombre
            )

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100), nullable=False)
    