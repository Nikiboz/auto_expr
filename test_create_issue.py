import requests
from base_API import BaseApi

class TestCreateIssue(BaseApi):

    def test_create_issue(self):
        url = self.base_url + '/issue'
        params = {
            'project': 'API',
            'summary': 'Regenerated',
            'decription': 'SkyNet is upon us'
        }

        r = requests.put(url,data=params,cookies=self.cookies)
        ID = r.headers['location'].split('/')[-1]

        self.assertEquals(r.status_code, 201)
        url = self.base_url + '/issue/' + ID
        r = requests.get(url, cookies=self.cookies)
        self.assertEquals(r.status_code, 200)