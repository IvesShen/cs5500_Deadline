import requests, json
import os, app, unittest, tempfile

#obj = {"where": {"text":"foob", "id":1}}
#obj = {"where": {"id":1}}
#obj = {"where": {"text":"test data"}}
obj = {"where": {"name":"admin"}, "orderby": "email desc", "limit":2, "offset": 2}
#print(json.dumps(obj))
#exit()
print("sending request")
#res = requests.get('http://localhost:5000/dual/1', json=json.dumps(obj))

sess = requests.session()
#res = sess.request('POST', 'http://localhost:5000/login', json=json.dumps({'email':'linus@expo.com','password':'confused'}))
res = sess.request('FETCH', 'http://localhost:5000/user', json=json.dumps(obj))

#res = requests.post('http://localhost:5000/dual', json={"text":"chai and biscuit."})
#res = requests.post('http://localhost:5000/dual', json={"text":"test data"})
#res = requests.put('http://localhost:5000/dual/5', json={"text":"ram chip."})
#res = requests.post('http://localhost:5000/user', json={"email":"foobar@nowhere.com", "password":"confused"})
#res = requests.post('http://localhost:5000/user', json={"name": "admin", "email":"linus@expo.com", "password":"confused"})
#res = requests.put('http://localhost:5000/user/2', json={"email":"doodle@nowhere.com", "password":"doodle"})
# res = requests.delete('http://localhost:5000/dual/1')
# res = requests.delete('http://localhost:5000/dual/2')
# res = requests.delete('http://localhost:5000/dual/4')
if res.ok:
    # print(res.json())
    d = res.json()
    if 'data' in d:
	for li in d['data']:
	    print(li)
    else:
	print(d)

class TestApp(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def testMain(self):
        response = self.app.get('/')
        self.assertEqual(b'Welcome to Pet Project!', response.get_data())

    def testInfo(self):
        response = self.app.get('/_info')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['Application'], "flask-based-pet-project 1.0.11")
        self.assertEqual(data['Powered By'], "flask 0.12.2, sqlalchemy 1.1.15")

    def loginForTest(self, email, password):
        dictionary = {
            "email": email,
            "password": password
        }
        json_data=json.dumps(dictionary)
        return self.app.post('/login', data=json_data)

    def testLogin(self):
        response = self.loginForTest("wrong@email.com", "???????")
        data = json.loads(response.get_data())
        self.assertEqual(data['status'], 'error')
        

if __name__ == '__main__':
    unittest.main()
