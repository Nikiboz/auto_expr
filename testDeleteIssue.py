from base_API import BaseApi

class DeleteIssue(BaseApi):

    def test_delete_issue(self):
        issue_Id = self.create_issue()

        url = self.base_url + '/issue/' + issue_Id
        r = self.request(url, 'delete')

        self.assertEquals(r.status_code, 200)

        r = self.request(url, 'get')
        self.assertEquals(r.status_code, 404)

    def test_delete_unexisting_issue(self):
        url = self.base_url + '/issue' + 'WTF'
        r = self.request(url, 'delete')
        self.assertEquals(r.status_code, 404)