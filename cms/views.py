from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json
from social.apps.django_app.default.models import  UserSocialAuth

def error404(request):
    return render(request, 'error404.html')

#Terminado
def inicio(request):
    pag = 1
    slider_cont = slider.objects.all().order_by('-pk')
    inicio = {
    'slider' : slider_cont,
    }
    return render(request, 'inicio.html', inicio)

#Terminado
def perfil(request, pk):
    favoritos = favorito.objects.filter(user_id=pk)
    valoracion = valoraciones.objects.filter(user_id=pk)
    us = get_object_or_404(User, pk=pk)
    try:
        cont = usuario.objects.get(user_id = pk)
        tipo = 'zinemas'
    except:
        cont = UserSocialAuth.objects.get(user=pk)
        tipo = 'facebook'
    perfil = {
    'contenido' : cont,
    'favoritos' : favoritos,
    'prm' : pk,
    'valoraciones' : valoracion,
    'tipo' : tipo,
    }
    return render(request, 'perfil.html', perfil)

#Terminado
def terminos(request):
    terminos = {
    }
    return render(request, 'terminos.html',terminos)

#Falta por terminar
def reproductor(request, pk):
    contenido = get_object_or_404(video, pk = pk)
    suma = contenido.vistas + 1
    contenido.vistas = suma
    contenido.save()
    reproductor = {
    'contenido' : contenido,
    }
    if request.method == "POST":
        userid = request.user
        relacion = usuario.objects.get(user_id=userid)
        contenido = request.POST.get("contenido", None)
        video_relacion = video.objects.get(pk=pk)
        crear_comentario = comentarios(cont=contenido, user_relacion=relacion, video_relacion=video_relacion)
        crear_comentario.save()
        return render(request, 'reproductor.html', reproductor)
    return render(request, 'reproductor.html', reproductor)

#Terminado
def entrar(request):
    error = ''
    if request.method == "GET":
        if request.GET.get("error") == "1":
            error = "El usuario o contraseña no coinciden"
    if request.user.is_authenticated():
        return redirect ('/')
    if request.method == "POST":
        pw = request.POST.get("pw", None)
        us = request.POST.get("us", None)

        try:
            user = authenticate(username = us, password = pw)
            login(request, user)
        except:
            return redirect('/login/?error=1')
        return redirect('/')
    entrar = {
    'error' : error,
    }
    return render(request, 'login.html', entrar)

def categoriam(request):
    if request.method == "GET":
        categoria = request.GET.get("categoria")
        if categoria == "accion":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "romance":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "infantil":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "terror":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "anime":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "documental":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "drama":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        elif categoria == "comedia":
            cate = {
            'categoria' : categoria,
            }
            return render(request, 'cate.html', cate)
        else:
            return HttpResponse("Error")
    else:
        return HttpResponse("Error")

def categorias(request):
    if request.method == "GET":
        pag = request.GET.get("pag")
        categoriam =  request.GET.get("categoria")
        if categoriam == "todos":
            lista = video.objects.order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                todo =  paginator.page(pag)
            except PageNotAnInteger:
                todo = paginator.page(1)
            except EmptyPage:
                todo = paginator.page(paginator.num_pages)
            cate ={
            'contenido': todo,
            'categoria':'todos',
            'tipo' : 'video',
            }
            if len(lista) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "vistas":
            lista = video.objects.order_by("-vistas")
            paginator = Paginator(lista,27)
            try:
                todo =  paginator.page(pag)
            except PageNotAnInteger:
                todo = paginator.page(1)
            except EmptyPage:
                todo = paginator.page(paginator.num_pages)
            cate ={
            'contenido': todo,
            'categoria':'vistas',
            'tipo' : 'video',
            }
            if len(lista) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "valoracion":
            lista = video.objects.order_by("-valoracion")
            paginator = Paginator(lista,27)
            try:
                todo =  paginator.page(pag)
            except PageNotAnInteger:
                todo = paginator.page(1)
            except EmptyPage:
                todo = paginator.page(paginator.num_pages)
            cate ={
            'contenido': todo,
            'categoria':'valoracion',
            'tipo' : 'video',
            }
            if len(lista) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "favoritos":
            lista = video.objects.order_by("-favoritos")
            paginator = Paginator(lista,27)
            try:
                todo =  paginator.page(pag)
            except PageNotAnInteger:
                todo = paginator.page(1)
            except EmptyPage:
                todo = paginator.page(paginator.num_pages)
            cate ={
            'contenido': todo,
            'categoria':'favoritos',
            'tipo' : 'video',
            }
            if len(lista) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "estreno":
            lista = categoria.objects.filter(categoria='Estreno').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'estreno',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "accion":
            lista = categoria.objects.filter(categoria='Accion').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'accion',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "romance":
            lista = categoria.objects.filter(categoria='Romance').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'romance',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "comedia":
            lista = categoria.objects.filter(categoria='Comedia').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'comedia',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "documental":
            lista = categoria.objects.filter(categoria='Documental').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'documental',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "drama":
            lista = categoria.objects.filter(categoria='Drama').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'drama',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "infantil":
            lista = categoria.objects.filter(categoria='Infantil').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'infantil',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "terror":
            lista = categoria.objects.filter(categoria='Terror').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'terror',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")
        if categoriam == "anime":
            lista = categoria.objects.filter(categoria='Anime').order_by("-pk")
            paginator = Paginator(lista,27)
            try:
                cont =  paginator.page(pag)
            except PageNotAnInteger:
                cont = paginator.page(1)
            except EmptyPage:
                cont = paginator.page(paginator.num_pages)
            cate ={
            'contenido':cont,
            'categoria':'anime',
            }
            if len(cont) > 0:
                return render(request, 'categoria.html', cate)
            else:
                return HttpResponse("No se encuentra ninguna pelicula de esta categoria")

#Terminado
def busqueda(request):
    if request.method == "GET":
        clave = request.GET.get('clave')
        clave = clave.lower()
        clavel = len(clave)
        resultados = video.objects.all()
        contenido = []
        for x in resultados:
            titulo =  x.titulo.lower()
            if titulo[0:clavel].find(clave) != -1:
                contenido.append(x)
        if len(contenido) > 0:
            page = True
            cont = contenido
        else:
            page = False
            cont =  "No se encontraron resultados para %s"%(clave)
        if  clavel < 2:
            page = False
            cont = "La busqueda debe tener como minimo 2 caracteres"
    busqueda = {
    'page' : page,
    'cont' : cont,
    'clave' : clave,
    }
    return render(request, 'resultados.html', busqueda)

#Terminado
def registro(request):
    #Para evitar errores a la hora de declarar mis errores
    contenido = 'ninguno'
    #Redireccionar en caso de que el usuario ya este logeado
    if request.user.is_authenticated():
        return redirect('/')
    #Si existe algun error durante el formulario retornar el error
    if request.method == "GET":
        error = request.GET.get("error")
        if error == '1':
            contenido = "Las claves no son iguales"
        elif error == '2':
            contenido = "El usuario debe ser mayor a 5 digitos"
        elif error == '3':
            contenido = "La clave debe ser mayor a 6 digitos"
        elif error == '4':
            contenido = "El usuario que introduciste ya existe"
        elif error == '5':
            contenido = "El correo que introduciste ya existe"
        elif error == '6':
            contenido = "Algun campo esta vacio"
    #Si existe el envio de el formulario realizar lo siguiente:
    if request.method == "POST":
        #Declarar los datos enviados en variables para ser tratadas
        pw = request.POST.get("pw", None)
        pw2 = request.POST.get("pw2", None)
        us = request.POST.get("us", None)
        email = request.POST.get("email", None)
        name =  request.POST.get("nombre")
        if len(us) == 0 or len(pw) == 0 or email == 0 or name == 0:
            return redirect('/registro/?error=6')
        if len(us) > 5:
            pass
        else:
            return redirect('/registro/?error=2')
        if len(pw) > 6:
            pass
        else:
            return redirect('/registro/?error=3')
        if pw == pw2:
            pass
        else:
            return redirect('/registro/?error=1')
        consultar_us = list(User.objects.filter(username = us))
        if len(consultar_us) > 0:
            return redirect('/registro/?error=4')
        else:
            pass

        consultar_email = list(User.objects.filter(email = email))
        if len(consultar_email) > 0:
            return redirect('/registro/?error=5')
        else:
            pass
        user = User.objects.create_user(username=us,password=pw,email=email,first_name=name)
        user.save()
        ok =  User.objects.get(username=us)
        usuariom = usuario(user_id=ok)
        usuariom.save()
        autentificarse = authenticate(username = us, password = pw)
        login(request, autentificarse )
        return redirect('/')
    registro = {
    'contenido' : contenido,
    }
    return render(request, 'registro.html', registro)

#   Mostrar las sugerencias por Ajax
def sugerencias(request):
    #   Tomar todos los nombres de los videos y crear una lista
    suger = list(video.objects.all())
    #   Tomar las primeras letras que se han solicitado
    sug = request.GET.get('sug')
    #   Cambiar las letras a minusculas
    sug = sug.lower()
    sugl = len(sug)
    #   Formateamos una lista para agregar posteriormente valores
    ok = []
    #   Si no se es mayor a 0 la palabra no devolver nada
    if len(sug)==0 :
        return HttpResponse("")
    #   Por cada item de suger(videos) se verifica si se tiene alguna relacion con el request
    for x in suger:
        x.titulo = x.titulo.lower()
        if x.titulo[0:sugl].find(sug) != -1:
            #Si se encuentra algun resultados se agregar valores en la lista
            ok.append("<a href='/reproductor/%s/'><p>%s</p></a>"%(x.pk , x.titulo))
    if len(ok) > 0:
        return HttpResponse(ok[:6])
    else:
        return HttpResponse("<p>No se encontraron resultados</p>")

#   Agrgar a favoritos un video
def agr_fav(request):
    #   Si el usuairo esta autenticado
    if request.user.is_authenticated():
        pass
    else:
        return redirect('/')
    #   Si se trata de un metodo GET
    if request.method == "GET":
        #   Tomamos los datos del metodo GET
        videom = request.GET.get("pk")
        user  = request.user.pk
        #   Tomamos el usuario que piido agregar a favoritos y el respectivo video
        usuariom = User.objects.get(pk=user)
        videox = video.objects.get(pk=videom)
        #   Verificar si ya se habia agragado a favoritos anteriormente
        consultar_fav = list(favorito.objects.filter(user=usuariom,video=videox ))
        if len(consultar_fav) > 0:
            return HttpResponse("")
        else:
            #   Guardar el dato
            listo =favorito(user=usuariom,video=videox)
            listo.save()
            #   Se suma al total de favoritos que tiene el video
            suma = videox.favoritos + 1
            videox.favoritos = suma
            videox.save()

def agr_valoracion(request):
    #   Si el usuairo esta autenticado
    if request.user.is_authenticated():
        pass
    else:
        return redirect('/')
    #   Si se trata de un metodo GET
    if request.method == "GET":
        #   Tomamos los datos del metodo GET
        videom = request.GET.get("pk")
        user  = request.user.pk
        #   Tomamos el usuario que piido agregar a valoracion y el respectivo video
        usuariom = User.objects.get(pk=user)
        videox = video.objects.get(pk=videom)
        #   Verificar si ya se habia agragado a favoritos anteriormente
        consultar_valoracion = list(valoraciones.objects.filter(user=usuariom,video=videox ))
        if len(consultar_valoracion) > 0:
            return HttpResponse("")
        else:
            #   Guardar el dato
            listo = valoraciones(user=usuariom,video=videox)
            listo.save()
            #   Se suma al total de valoraciones que tiene el video
            suma = videox.valoracion + 1
            videox.valoracion = suma
            videox.save()

#   Sin uso alguno
def actualizar_perfil(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", None)
        email = request.POST.get("email", None)
        clave = request.POST.get("clave", None)
        clave2 = request.POST.get("clave2", None)
        try:
            foto = request.FILES['perfil']
        except:
            foto='none'
        actualizar = User.objects.get(username=request.user.username)
        actualizar2 = usuario.objects.get(user_id=request.user.pk)
        log = []
        log_error = []

        #Checar la clave
        if len(clave) > 0:
            if len(clave) > 5:
                if(clave == clave2):
                    actualizar.set_password(clave)
                    actualizar.save()
                    log.append("Se cambio la clave actual por %s correctamente"%(clave))
                else:
                    log_error.append("Las claves introducidas no son iguales")
            else:
                #Marcar error
                log_error.append("Tu clave debe ser mayor a 5 digitos")

        #Checar el usuario
        if len(nombre) > 0:
            if len(nombre) < 4:
                #Marcar error
                log_error.append("Tu nombre debe ser mayor  a 4 digitos")
            if len(nombre) > 15:
                #Marcar error
                log_error.append("Tu nombre debe ser menor a 15 caracteres")
            consultar_us = list(User.objects.filter(username = nombre))
            if len(consultar_us) > 0:
                #Ralizar un error
                log_error.append("El usuario ya existe")
            else:
                actualizar.username = nombre
                actualizar.save()
                log.append("Se guardo el nombre del usuario con exito")
        #Checar el email
        if len(email) > 0 and len(email) > 4:
            if len(email) > 25:
                #Marcar error
                log_error.append("Tu correo debe ser menor a 25 caracteres")
            consultar_email = list(User.objects.filter(email = email))
            if len(consultar_email) > 0:
                #Ralizar un error
                log_error.append("El correo ya existe")
            else:
                actualizar.email = email
                actualizar.save()
                log.append("Se guardo el correo electronico con exito")
        #Checar el perfil
        if foto != 'none':
            terminacion = foto.name
            cant = len(terminacion)
            cont = len(terminacion) - 3
            ultima = terminacion[cont:cant]
            if ultima == 'png' or ultima == 'gif' or ultima == 'jpg' or ultima == 'peg':
                actualizar2.perfil = foto
                actualizar2.save()
                log.append('Se cambio la foto de portada a ' + terminacion)
            else:
                log_error.append('no se aceptan terminaciones ' + ultima)

        if len(log_error) > 0:
            error = True
        else:
            error = False
        if len(log) == 0 and len(log_error) == 0:
            error= True
            log_error.append("No se introdujo ningun dato")

        return render(request, 'act.html', {'log' : log, 'error' : error, 'log_error' : log_error,})
    else:
        return redirect('/')
