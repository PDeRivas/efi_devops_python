from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    url_for
)

from app import app, db

from app.models.models import (
    Usuario,
    Post,
    Categoria,
    Comentario,
)

"""from app.schemas.schema import (
    PostSchema,
    UserSchema,
)"""

from datetime import datetime

@app.context_processor
def inject_categorias():
    categorias = db.session.query(Categoria).all()
    return dict(
        categorias = categorias
    )

@app.context_processor
def inject_posts():
    posts = db.session.query(Post).all()
    posts = reversed(posts)
    return dict(
        posts = posts
    )

@app.context_processor
def inject_comentarios():
    comentarios = db.session.query(Comentario).all()
    return dict(
        comentarios = comentarios
    )

@app.route('/')
def index():
   return render_template(
       'index.html'
    )

@app.route('/inicio_sesion', methods=['POST'])
def iniciar_sesion():
    if request.method == 'POST':
        email_usuario = request.form['email']
        clave_usuario = request.form['clave']
        usuarios = db.session.query(Usuario).filter_by(
                    correo = email_usuario,clave = clave_usuario
                    ).all()
        try:
            usuario_id = usuarios[0].id
            return redirect(url_for('inicio', usuario_id = usuario_id))
        except:
            return redirect(url_for('index'))

@app.route("/registro", methods=['POST'])
def registro():
    if request.method=='POST':
        return render_template(
            'registrarse.html'
        )

@app.route('/registrarse', methods=['POST'])
def registrarse():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre']
        email_usuario = request.form['email']
        clave_usuario = request.form['clave']
        
        #Instancia
        nuevo_usuario = Usuario(nombre = nombre_usuario, 
                                correo = email_usuario,
                                clave = clave_usuario)
        #Agregar Instancia
        db.session.add(nuevo_usuario)
        #Guardar Instancia 
        db.session.commit()
    return(redirect(url_for('index')))

@app.route('/inicio')
def inicio():
    usuario_id = request.args['usuario_id']
    usuario_id = int(usuario_id)
    usuario = db.session.query(Usuario).filter_by(
              id = usuario_id
              ).all()
    
    usuario_nombre = usuario[0].nombre
    return render_template(
        'inicio.html',
        usuario_id = usuario_id,
        usuario_nombre = usuario_nombre,
        logeado = True
    )

@app.route('/crear_post', methods=['POST'])
def crear_post():
    if request.method=='POST':
        usuario_id = request.form['usuario_id']
        
        titulo = request.form['titulo']        
        contenido = request.form['contenido']       
        categoria_id = request.form['categoria']

        fecha = datetime.now()
        
        #Instancia
        nuevo_post = Post(titulo = titulo, 
                          contenido = contenido, 
                          fecha_creacion = fecha, 
                          autor_id = usuario_id, 
                          categoria_id = categoria_id)
        #Agregar Instancia
        db.session.add(nuevo_post)
        #Guardar Instancia
        db.session.commit() 
        return redirect(url_for('inicio', usuario_id = usuario_id))
    

@app.route('/crear_comentario', methods=['POST'])
def crear_comentario():
    if request.method=='POST':
        contenido = request.form['contenido']       
        fecha = datetime.now()
        usuario_id = request.form['usuario_id']
        post_id = request.form['post_id']
        
        #Instancia
        nuevo_comentario = Comentario(texto_comentario = contenido,
                                      fecha_creacion = fecha, 
                                      autor_id = usuario_id, 
                                      post_id = post_id)
        #Agregar Instancia
        db.session.add(nuevo_comentario)
        #Guardar Instancia
        db.session.commit() 
        return redirect(url_for('inicio', usuario_id = usuario_id))

@app.route("/borrar_post", methods=['POST'])
def borrar_post():
    if request.method=='POST':
        usuario_id = request.form['usuario_id']
        
        post_id = request.form['post_id']

        comentarios = db.session.query(Comentario).filter_by(
                      post_id = post_id
                      ).all()
        for comentario in comentarios:
            db.session.delete(comentario)
            db.session.commit()
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()

        return redirect(url_for('inicio', usuario_id = usuario_id))

@app.route("/editar", methods=['POST'])
def editar():
    if request.method=='POST':
        usuario_id = request.form['usuario_id']
        post_id = request.form['post_id']
        post = Post.query.get(post_id)
        titulo = post.titulo
        contenido = post.contenido
        return render_template(
            'editar.html',
            titulo = titulo,
            contenido = contenido,
            usuario_id = usuario_id,
            post_id = post_id,
            logeado = True
        )
    
@app.route("/editar_post", methods=['POST'])
def editar_post():
    if request.method=='POST':
        usuario_id = request.form['usuario_id']
        post_id = request.form['post_id']
        titulo_editado = request.form['titulo_editado']
        contenido_editado = request.form['contenido_editado']

        post = Post.query.get(post_id)
        post.titulo = titulo_editado
        post.contenido = contenido_editado
        db.session.commit()

    return redirect(url_for('inicio', usuario_id = usuario_id))