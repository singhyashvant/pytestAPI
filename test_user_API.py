import requests


class TestUsersAPI:

    def test1(self, base_url):
        url = base_url + '/public-api/users'
        response = requests.get(url)
        print(response)
        assert response.status_code == 200, "Bad status code"

    def test_post(self, base_url):
        url = base_url + '/public-api/users'
        body = '{"name":"Tenali Ramakrishna", "gender":"Male", "email":"tenali.ramakrishna@15ce.com", ' \
               '"status":"Active"} '
        response = requests.post(url, data=body)
        print(response)
        assert response.status_code == 200, "Bad status code"
        data = response.json()
        assert data['code'] == 200, "Fail, code has not matched"

    def test_get(self, base_url):
        url = base_url + '/public-api/users/123'
        response = requests.get(url)
        print(response)
        assert response.status_code == 200, "Bad status code"
        data = response.json()
        assert data['code'] == 200, "Fail, code has not matched"

    def test_put(self, base_url):
        url = base_url + '/public-api/users/123'
        response = requests.put(url)
        print(response)
        assert response.status_code == '200', "Bad status code"
        data = response.json()
        assert data['code'] == 200, "Fail, code has not matched"

    def test_delete(self, base_url):
        url = base_url + 'public-api/users/123'
        response = requests.delete(url)
        print(response)
        assert response.status_code == 200, "Bad status code"
        data = response.json()
        assert data['code'] == 200, "Fail, code has not matched"
