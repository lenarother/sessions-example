import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCountView:

    def test_get(self, client):
        url = reverse('counter')

        response = client.get(url)
        assert response.status_code == 200
        assert response.context['counter'] == 1

        client.get(url)
        client.get(url)
        client.get(url)

        response = client.get(url)
        assert response.context['counter'] == 5

        client.cookies.pop('sessionid')
        response = client.get(url)
        assert response.context['counter'] == 1
