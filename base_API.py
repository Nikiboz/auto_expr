import unittest
import requests
import xmltodict
from yaml import load

class BaseApi(unittest.TestCase):

    def setUp(self):
        self.settings = load(open('setup.yaml').read())
        self.base_url = self.settings['base_url']
        self.cookies = self._login()

    def _login(self):
        url = self.base_url + '/user/login'
        params = {
            "login": self.settings['credentials']['login'],
            "password": self.settings['credentials']['password']
        }
        r = requests.post(url, data=params)

        return r.cookies

    def create_issue(self):

        url = self.base_url + '/issue'
        params = {
            'project': 'API',
            'summary': 'Regenerated',
            'decription': 'SkyNet is upon us'
        }

        r = requests.put(url, data=params, cookies=self.cookies)
        issue_Id = r.headers['location'].split('/')[-1]
        self.assertEquals(r.status_code, 201)

        return issue_Id

    def request(self, url, method, params=None):
       # method in ('get', 'post', 'put', 'delete')
       return getattr(requests, method)(url, data=params, cookies=self.cookies)