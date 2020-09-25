import datetime
import json
from time import strftime

import pytest
from django.urls import reverse
from django_mock_queries.query import MockSet
from rest_framework.exceptions import ValidationError

from lista.models import Artista
from lista.serializers import ArtistaSerializer
from lista.views import ArtistaViewSet

class TestArtistaManager:

    def test_get_artista_by_created(self, mocker):
        expected_results = [Artista(Nombre='Mike', Apellidos='Posner', Celular='987658495', Correo='mike.posner@hotmail.com')]

        date = strftime('%Y-%m-%d')
        # django-mock-queries nos permite crear Mock QuerySets
        # para omitir el acceso a BD
        qs = MockSet(expected_results[0])

        # Patch el metodo qet_queryset para modificar su comportamiento
        # y que nos retorne nuestro queryset  y asi omitir el acceso
        # a BD
        mocker.patch.object(Artista.objects, 'get_queryset', return_value=qs)

        result = list(Artista.objects.get_artista_by_created(date))

        assert result == expected_results
        assert str(result[0]) == expected_results[0].Nombre

class TestArtistaSerializer:
    def test_expected_serialized_json(self):
        expected_results = {
            'id': 1,
            'Nombre': 'Mike',
            'Apellidos': 'Posner',
            'Celular': '987658495',
            'Correo': 'mike.posner@hotmail.com'
        }
        artista = Artista(**expected_results)
        results = ArtistaSerializer(artista).data
        assert results == expected_results

    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            'Nombre': 'Mike',
            'Apellidos': 'Posner',
            'Celular': '987658495'
        }

        serializer = ArtistaSerializer(data=incomplete_data)

        # Este ContextManager nos permite verificar que
        # se ejecute correctamente una Excepcion
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)

class TestViewSet:

    @pytest.mark.urls('lista.urls')
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
            Artista(id=1, Nombre='Mike', Apellidos='Posner', Celular='987658495', Correo='mike.posner@hotmail.com'),
            Artista(id=2, Nombre='Mike', Apellidos='Posner', Celular='987658495', Correo='mike.posner@hotmail.com')
        )

        mocker.patch.object(ArtistaViewSet, 'get_queryset', return_value=queryset)
        response = ArtistaViewSet.as_view({'get': 'list'})(request).render()

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2

    # Este helper de la libreria django-pytest, nos permite olvidarnos
    # de los namespaces de las urls de django, y utilizar un archivo
    # urls.py definido.
    @pytest.mark.urls('lista.urls')
    @pytest.mark.django_db(transaction=True)
    def test_create(self, rf, mocker):
        url = reverse('artista-list')

        data = {
                "Nombre": "Mike",
                "Apellidos": "Posner",
                "Celular": "987658495",
                "Correo": "mike.posner@hotmail.com"
                }

        request = rf.post(url,
                          content_type='application/json',
                          data=json.dumps(data))

        mocker.patch.object(Artista, 'save')
        # Renderizamos la vista con nuestro request.
        response = ArtistaViewSet.as_view({'post': 'create'})(request).render()

        assert response.status_code == 201
        assert json.loads(response.content).get('Nombre') == 'Jhon'
        # Verificamos si efectivamente se llamo el metodo save
        assert Artista.save.called

    @pytest.mark.urls('lista.urls')
    def test_update(self, rf, mocker):
        url = reverse('artista-detail', kwargs={'pk': 1})
        request = rf.patch(url,
                           content_type='application/json',
                           data=json.dumps({'Nombre': 'Mike'}))
        artista = Artista(id=1, Nombre='Mike', Apellidos='Posner', Celular='987658495', Correo='mike.posner@hotmail.com')

        # Patch al metodo get_object de nuestro ViewSet para
        # para omitir el acceso a BD
        # Lo mismo para el motodo save() de nuestro modelo Car
        
        mocker.patch.object(ArtistaViewSet, 'get_object', return_value=artista)
        mocker.patch.object(Artista, 'save')

        response = ArtistaViewSet \
            .as_view({'patch': 'partial_update'})(request).render()

        assert response.status_code == 200
        assert json.loads(response.content).get('Nombre') == 'Mike'
        assert Artista.save.called

    @pytest.mark.urls('lista.urls')
    def test_delete(self, rf, mocker):
        url = reverse('artista-detail', kwargs={'pk': 1})
        request = rf.delete(url)

        artista = Artista(id=1, Nombre='Mike', Apellidos='Posner', Celular='987658495', Correo='mike.posner@hotmail.com')

        # De nuevo hacemos patch al metodo get_object
        # y tambien al delete del objeto.
        mocker.patch.object(ArtistaViewSet, 'get_object', return_value=artista)
        mocker.patch.object(Artista, 'delete')

        response = ArtistaViewSet.as_view({'delete': 'destroy'})(request).render()

        assert response.status_code == 204
        assert Artista.delete.called
