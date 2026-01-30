from app import app


# first test case to check the hello route
def test_hello_route_sucess():
    tester = app.test_client()
    response = tester.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'


data= {
    'gestation': [38],
    'parity': [1],
    'age': [25],
    'height': [65],
    'weight': [120],
    'smoke': [0]
}
# second test case to check the predict route
def test_predict_route_sucess():
    tester=app.test_client()
    responce=tester.post('/predict', json=data)
    assert responce.status_code==200
    assert responce.data is not None

def test_predict_route_fail():
    tester=app.test_client()
    responce=tester.post('/predict', json={})
    assert responce.status_code==500