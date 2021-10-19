import django
from django.contrib                 import admin
from django.urls                    import path, include
from authAppExample                 import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authAppExample.views.views           import inicio, crearInmueble, editarInmueble,eliminarInmueble, perfil,register


urlpatterns = [
    
    path('admin/',                                  admin.site.urls),  # use defaul Djando Admin
    path('login/',                                  TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                TokenRefreshView.as_view()), # generate new access token
    path('user/',                                   authAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                          authAppViews.UserDetailView.as_view()), # check info for an specific user based on id(pk)
    #path('transaction/',                            authAppViews.TransactionCreateView.as_view()), # create a new transaction
    #path('transaction/<int:user>/<int:pk>/',        authAppViews.TransactionsDetailView.as_view()), # view information for a transaction
    #path('transactions/<int:user>/<int:account>/',  authAppViews.TransactionsAccountView.as_view()), # view all transactions for an specific account
    #path('transaction/update/<int:user>/<int:pk>/', authAppViews.TransactionsUpdateView.as_view()), # update a transaction
    #path('transaction/remove/<int:user>/<int:pk>/', authAppViews.TransactionsDeleteView.as_view()), # delete a transaction
    path('',inicio,name='index'),
    path('crear_inmueble/',crearInmueble,name='crear_inmueble'),
    path('perfil/crear_inmueble/',crearInmueble,name='crear_inmueble'),
    path('editar_inmueble/<int:id>/',editarInmueble, name='editar_inmueble'),
    path('eliminar_inmueble/<int:id>/',eliminarInmueble,name='eliminar_inmueble'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('perfil/', perfil, name = 'perfil'),
    path('register/', register, name='register'),
]