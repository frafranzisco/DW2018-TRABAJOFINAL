
from django.shortcuts import render, redirect
from book.models import *
from book.forms import BookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.template import RequestContext, loader
# from django.contrib import messages
# Create your views here.

@login_required(login_url="/")
def inicio(request):
	object_list = Book.objects.all() 
	template_name = "inicio.html"
	return render(request, template_name, {'object_list':object_list})
def add_genre(request):
	template_name = "genre.html"
	data = {}
	object_list = Book.objects.all()
	data['add_genre'] = object_list
	return render(request,template_name,data)

@login_required(login_url="/")
def detail_book(request,id):
	template_name = "detail_book.html"
	data = {}
	book = Book.objects.get(id=id)
	print(book)
	data['detail_book']=book
	return render(request,template_name,data)
@login_required(login_url="/")	
def list_book(request):
	object_list = Book.objects.all().order_by('-id')				#LISTA
	paginator = Paginator(object_list, 3) 							#PARA MOSTRAR 3 POR PAGINA
	page = request.GET.get('page')									#PASA SABER QUÉ PÁGINA EN F(X) DE REGISTROS
	data = {}
	template_name = 'list_book.html'
	try:
		b = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		b = paginator.page(1)
	except EmptyPage:
		# If page is out of rangAPRETARe (e.g. 9999), deliver last page of results.
		b = paginator.page(paginator.num_pages)
	data['object_list'] = object_list
	data['b'] = b
	return render(request, template_name, data)
@login_required(login_url="/")
def add_book(request):
	template_name = 'add_book.html'
	data={}
	if request.method == "POST":
		form = BookForm(request.POST, request.FILES)
		if form.is_valid():
			user = User.objects.get(username=request.user.username)
			user_profile = UserProfile.objects.get(user=user)
			user_book = UserBook.objects.get(user=user_profile)
			title = form.cleaned_data.get('title')
			author = form.cleaned_data.get('author')
			editorial = form.cleaned_data.get('editorial')
			book_type = form.cleaned_data.get('book_type')
			genre = form.cleaned_data.get('genre')
			language = form.cleaned_data.get('language')
			original = form.cleaned_data.get('original')
			transaction = form.cleaned_data.get('transaction')
			price = form.cleaned_data.get('price')
			comment = form.cleaned_data.get('comment')
			number_of_pages = form.cleaned_data.get('number_of_pages')
			picture = form.cleaned_data.get('picture')
			book = Book.objects.create(user=user_book,
				title=title,
				author=author,
				editorial=editorial,
				book_type=book_type,
				genre=genre,
				language=language,
				original=original,
				transaction=transaction,
				price=price,
				comment=comment,
				number_of_pages=number_of_pages,
				picture=picture)
			book.save
			return redirect('list_book')
	else:
		form = BookForm()
	data['form'] = form
	return render(request, template_name, data)


#
#
# #HAY QUE HACER FUNCIONAR EL BOTÓN DE AGREGAR LIBRO EN LIST_BOOK
#
#
# def update_book(request,id):
# 	data = {}
# 	book = Book.objects.get(id=id)
# 	if request.method == "GET":
# 		data['form'] = BookForm(instance=book)
# 	else:
# 		data['form']= BookForm(request.POST,request.FILES, instance=book)
# 		b = data['form']
# 		if b.is_valid():
# 			b.save()
# 		return redirect('list_book')
# 	template_name = 'add_book.html'
# 	return render(request, template_name, data)
#
#
#
# def delete_book(request,id):
# 	b = Book.objects.get(id=id)
#
# 	if Book.objects.filter(id=id).exists():
# 		b = Book.objects.get(id=id)
# 		b.delete()
# 	else:
# 		print("No existe")
#
# 	return redirect('list_book')
#
#
# def prueba(request):
#     template_name = "prueba.html"
#     return render(request,template_name)

# Create your views here.
#

#####USERBOOK#####
@login_required(login_url="/")
def list_user(request):
    template_name = 'list_user.html'
    data = {}
    data['form'] = BookForm()
    object_list = UserBook.objects.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    data['object_list','users'] = object_list, users
    return render(request,template_name,data)
@login_required(login_url="/")
def remove_user(request,userbook_run):
    template_name = "book/remove_user.html"
    data = {}
    user_remove = UserBook.objects.get(RUN=user_run)
    data['user'] = user_remove
    if request.method == "POST":
        user_remove.delete()
        return redirect("user_list")
    return render(request,template_name,data)
@login_required(login_url="/")
def edit_user(request,userbook_run):
    template_name = 'book/add_user.html'
    data = {}
    user = UserBook.objects.get(rut=user_run)
    if request.method == "GET":
        form_user = BookForm(instance=user)
    else:
        form_user = BookForm(request.POST,request.FILES, instance=user)
        if form_user.is_valid():
            form_user.save()
        return redirect("user_list")
    data['form']=form_user
    return render(request,template_name,data)
@login_required(login_url="/")
def add_user(request):
    template_name = 'book/add_user.html'
    data = {}
    if request.method == "POST":
        form_user = BookForm(request.POST,request.FILES)
        if form_user.is_valid():
            form_user.save()
            return redirect("home")
    else:
        data['form'] = BookForm()
    return render(request,template_name,data)
#####USERBOOK#####
