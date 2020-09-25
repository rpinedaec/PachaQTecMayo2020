from django.test import TestCase
import datetime
import json
from time import strftime
import pytest
from django.urls import reverse
# from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError

from hrkapp.models import artista, album, cancion, user, playlist, canciondeplaylist
from hrkapp.serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer, UserSerializer, PlaylistSerializer, CancionDePlaylistSerializer
from hrkapp.views import ArtistaViewSet, AlbumViewSet, CancionViewSet, UserViewSet, PlaylistViewSet, CancionDePlaylistViewSet

class TestCancionViewSet:

    @pytest.mark.urls('hrkprj.urls')
    def test_list(self, rf, mocker):
        #  django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('cancion-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            cancion(nombre='stitches', genero='pop', artista='ariana grande', album='3rings'),
            cancion(nombre='stitches', genero='pop', artista='ariana grande', album='3rings')
        )

        mocker.patch.object(CancionViewSet, 'get_queryset', return_value=queryset)
        response = CancionViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('hrkprj.urls')
    @pytest.mark.django_db(transaction=True)
    def test_create(self, rf, mocker):
        url = reverse('cancion-list')

        data = {
            'nombre': 'stitches',
            'genero': 'pop',
            'artista':'ariana grande',
            'album': '3rings'
        }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(cancion, 'save')
        # Renderizamos la vista con nuestro request.
        response = CancionViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('nombre') == 'stitches'
        # Verificamos si efectivamente se llamo el metodo save
        assert cancion.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_update(self, rf, mocker):
        url = reverse('cancion-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'name': 'fmilla'}))
        can = cancion(id=1,
                  nombre='lol',
                  genero='rock',
                  artista='ariana grande',
                  album='3rings',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Car
        
        mocker.patch.object(CancionViewSet, 'get_object', return_value=can)
        mocker.patch.object(cancion, 'save')

        response = CancionViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'fmilla'
        assert cancion.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_delete(self, rf, mocker):
        url = reverse('cancion-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        can = cancion(id=1,
                  nombre='lol',
                  genero='rock',
                  artista='ariana grande',
                  album='3rings',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(CancionViewSet, 'get_object', return_value=can)
        mocker.patch.object(cancion, 'delete')

        response = CancionViewSet \
            .as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert cancion.delete.called

class TestArtistaViewSet:
    
    @pytest.mark.urls('hrkprj.urls')
    def test_list(self, rf, mocker):
        #  django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('artista-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            artista(nombre='carina', nacionalidad='peruana'),
            artista(nombre='carina', nacionalidad='peruana')
        )

        mocker.patch.object(ArtistaViewSet, 'get_queryset', return_value=queryset)
        response = ArtistaViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('hrkprj.urls')
    @pytest.mark.django_db(transaction=True)
    def test_create(self, rf, mocker):
        url = reverse('artista-list')

        data = {
            'nombre': 'carina',
            'nacionalidad': 'peruana'
        }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(artista, 'save')
        # Renderizamos la vista con nuestro request.
        response = ArtistaViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('nombre') == 'carina'
        # Verificamos si efectivamente se llamo el metodo save
        assert artista.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_update(self, rf, mocker):
        url = reverse('artista-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'name': 'fmilla'}))
        art = artista(id=1,
                  nombre='sofia',
                  nacionalidad='alemana',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Car
        
        mocker.patch.object(ArtistaViewSet, 'get_object', return_value=art)
        mocker.patch.object(artista, 'save')

        response = ArtistaViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'fmilla'
        assert artista.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_delete(self, rf, mocker):
        url = reverse('artista-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        art = artista(id=1,
                  nombre='sofia',
                  nacionalidad='alemana',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(ArtistaViewSet, 'get_object', return_value=art)
        mocker.patch.object(artista, 'delete')

        response = ArtistaViewSet \
            .as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert artista.delete.called

class TestAlbumViewSet:
    
    @pytest.mark.urls('hrkprj.urls')
    def test_list(self, rf, mocker):
        #  django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('album-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            album(nombre='3rings'),
            album(nombre='3rings')
        )

        mocker.patch.object(AlbumViewSet, 'get_queryset', return_value=queryset)
        response = AlbumViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('hrkprj.urls')
    @pytest.mark.django_db(transaction=True)
    def test_create(self, rf, mocker):
        url = reverse('album-list')

        data = {
            'nombre': '3rings'
        }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(album, 'save')
        # Renderizamos la vista con nuestro request.
        response = AlbumViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('nombre') == '3rings'
        # Verificamos si efectivamente se llamo el metodo save
        assert artista.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_update(self, rf, mocker):
        url = reverse('album-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'name': 'fmilla'}))
        alb = album(id=1,
                  nombre='2rings',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Car
        
        mocker.patch.object(AlbumViewSet, 'get_object', return_value=alb)
        mocker.patch.object(album, 'save')

        response = AlbumViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'fmilla'
        assert album.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_delete(self, rf, mocker):
        url = reverse('album-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        alb = album(id=1,
                  nombre='2rings',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(AlbumViewSet, 'get_object', return_value=alb)
        mocker.patch.object(album, 'delete')

        response = AlbumViewSet \
            .as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert album.delete.called

class TestUserViewSet:
    
    @pytest.mark.urls('hrkprj.urls')
    def test_list(self, rf, mocker):
        #  django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('user-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            user(nombre='juana',correo='jna@gmail.com'),
            user(nombre='juana',correo='jna@gmail.com')
        )

        mocker.patch.object(UserViewSet, 'get_queryset', return_value=queryset)
        response = UserViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('hrkprj.urls')
    @pytest.mark.django_db(transaction=True)
    def test_create(self, rf, mocker):
        url = reverse('user-list')

        data = {
            'nombre': 'juana',
            'correo':'jna@gmail.com'
        }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(user, 'save')
        # Renderizamos la vista con nuestro request.
        response = UserViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('nombre') == 'juana'
        # Verificamos si efectivamente se llamo el metodo save
        assert user.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_update(self, rf, mocker):
        url = reverse('user-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'name': 'fmilla'}))
        use = user(id=1,
                  nombre='pepe',
                  correo='pp@gmail.com',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Car
        
        mocker.patch.object(UserViewSet, 'get_object', return_value=use)
        mocker.patch.object(user, 'save')

        response = UserViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'fmilla'
        assert user.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_delete(self, rf, mocker):
        url = reverse('user-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        use = user(id=1,
                  nombre='pepe',
                  correo='pp@gmail.com',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(UserViewSet, 'get_object', return_value=use)
        mocker.patch.object(user, 'delete')

        response = UserViewSet \
            .as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert user.delete.called

class TestPlaylistViewSet:
    
    @pytest.mark.urls('hrkprj.urls')
    def test_list(self, rf, mocker):
        #  django-pytest nos permite pasar por inyeccion de dependencia
        # a nuestros tests algunos objetos, en este caso le "INYECTE"
        # el objeto rf que no es mas que el comun RequestFactory
        # y mocker que nos permite hacer patch a objetos y funciones
        url = reverse('playlist-list')
        request = rf.get(url)

        # usamos la libreria django-mock-queries para crear un Mock
        # de nuestro queryset y omitir el acceso a BD

        queryset = MockSet(
            playlist(nombre='verano',user='pepe'),
            playlist(nombre='verano',user='pepe')
        )

        mocker.patch.object(PlaylistViewSet, 'get_queryset', return_value=queryset)
        response = PlaylistViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('hrkprj.urls')
    @pytest.mark.django_db(transaction=True)
    def test_create(self, rf, mocker):
        url = reverse('playlist-list')

        data = {
            'nombre': 'verano',
            'user':'pepe'
        }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(playlist, 'save')
        # Renderizamos la vista con nuestro request.
        response = PlaylistViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('nombre') == '3rings'
        # Verificamos si efectivamente se llamo el metodo save
        assert playlist.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_update(self, rf, mocker):
        url = reverse('playlist-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'name': 'fmilla'}))
        alb = playlist(id=1,
                  nombre='invierno',
                  user='pepe',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Car
        
        mocker.patch.object(PlaylistViewSet, 'get_object', return_value=alb)
        mocker.patch.object(playlist, 'save')

        response = PlaylistViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('name') == 'fmilla'
        assert playlist.save.called

    @pytest.mark.urls('hrkprj.urls')
    def test_delete(self, rf, mocker):
        url = reverse('album-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        alb = playlist(id=1,
                  nombre='invierno',
                  user='pepe',
                  created=datetime.datetime.now(),
                  modified=datetime.datetime.now())

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(PlaylistViewSet, 'get_object', return_value=alb)
        mocker.patch.object(playlist, 'delete')

        response = PlaylistViewSet \
            .as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert playlist.delete.called

class TestSearchFields:
    
    def test_for_valid_search_fields(self):
        # It is easy to add a foreignkey in a search field instead of a
        # stringfield on the class the foreign key points to.
        for model_artista_class in [
                # Hardcoded list
                hrkapp.artista]:
            artita_class = model_artista_class.model
            print("Testing search fields for %s" % artita_class)
            for fieldname in model_artista_class.search_fields:
                query = '%s__icontains' % fieldname
                print("Testing with %s" % query)
                kwargs = {query: 'reinout'}
                # We have no content, so the number of results if we search on
                # something should be zero. The only thing that matters is
                # that we get no 'cannot search on foreignkey' error.
                self.assertEquals(
                    artita_class.objects.filter(**kwargs).count(),
                    0)