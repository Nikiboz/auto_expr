from base_API import BaseApi

class BaseTest(BaseApi):

    def setUp(self):
        self.baseUrl = 'https://codespace-api.myjetbrains.com/youtrack/rest'
        self.creds = ('root', 'c11desp@ce')

    def test_get_issue(self):
        id = 'API-1'
        url = self.baseUrl + '/issue/' + 'API-1'
        response = self.requests.get(url, auth=self.creds)
        response_dict = self.xmltodict.parse(response.text)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response_dict['issue']['@id'], id)

    def test_get_issue_inval_id(self):
        url  = self.baseUrl + '/issue/' + 'WTF'
        r = self.requests.get(url, auth=self.creds)

        self.assertEquals(r.status_code, 404)