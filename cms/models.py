from django.db import models
from django.contrib.auth.models import User


class usuario(models.Model):
    perfil = models.ImageField(upload_to='perfil', default='perfil/default.png')
    portada = models.ImageField(upload_to='portada', default='portada/default.png')
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.user_id.username

class video(models.Model):
    titulo = models.CharField(max_length=140)
    sinopsis = models.TextField(max_length=1200)
    poster = models.ImageField(upload_to='posters')
    url = models.CharField(max_length=800)
    descarga = models.CharField(max_length=800)
    fecha = models.DateTimeField(auto_now=True)
    trailer = models.CharField(max_length=800)
    vistas = models.IntegerField(default=0)
    favoritos =  models.IntegerField(default=0)
    valoracion = models.IntegerField(default=0)
    fecha = models.CharField(max_length=40) 
    calidad = (
    ('HD', 'HD'),
    ('TSCREEN', 'TSCREEN'),
    ('DVDRIP', 'DVDRIP'),
    ('HDTS', 'HDTS'),
    )
    calidad = models.CharField(max_length=50, choices=calidad)

    def __str__(self):
        return self.titulo

class categoria(models.Model):
    videopk = models.ForeignKey(video)
    categoriass = (
    ('Accion', 'Accion'),
    ('Estreno', 'Estreno'),
    ('Comedia', 'Comedia'),
    ('Terror', 'Terror'),
    ('Anime', 'Anime'),
    ('Romance', 'Romance'),
    ('Documental', 'Documental'),
    ('Infantil', 'Infantil'),
    ('Drama', 'Drama'),
    )
    categoria = models.CharField(max_length=122, choices=categoriass)

    def __str__(self):
        return "%s | %s " %(self.videopk.titulo, self.categoria)

class slider(models.Model):
    titulo = models.CharField(max_length=140)
    videopk = models.ForeignKey(video)
    fondo = models.ImageField(upload_to='fondos')
    def __str__(self):
        return self.titulo

class favorito(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(video)

    def __str__(self):
        return "%s | %s" %(self.user, self.video)

class valoraciones(models.Model):
    user = models.ForeignKey(User)
    video = models.ForeignKey(video)

    def __str__(self):
        return "%s | %s" %(self.user, self.video)


 
