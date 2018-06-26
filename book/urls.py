from django.urls import path
from book import views

urlpatterns = [
    
	path('inicio/', views.inicio, name="inicio"),
	path('list_book', views.list_book, name="list_book"),
    path('add_book/', views.add_book, name="add_book"),
	# path('update_book/<str:id>', views.update_book, name="update_book"),
	# path('delete_book/<str:id>', views.delete_book, name="delete_book"),
	path('detail_book/<str:id>', views.detail_book, name="detail_book"),
	#HAY QUE HACER FUNCIONAR EL BOTÓN DE AGREGAR LIBRO EN LIST_BOOK
	#path('index',views.index,name="index"),
	path('genre/',views.add_genre,name="genre"),
	#CRUD BOOKUSER
	path('add_user/',views.add_user,name='user_add'),
    path('list_user/',views.list_user,name='user_list'),
    path('edit_user/<str:user_run>',views.edit_user,name='user_edit'),
    path('remove_user/<str:user_run>',views.remove_user,name='user_remove'),
]
