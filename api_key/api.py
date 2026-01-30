# middleware/ decorator functon  to verify api key for every request
import app


API_KEY ="myapikey"
def verify_api_key(func):
    def wrapper(*args,**kwargs):
        request_api_key=request.headers.get('x-api-key')
        if request_api_key==API_KEY:
            return func(*args,**kwargs)
        else:
            return jsonify({'error':'Unauthorized access'}),401
    return wrapper

@app.route('/profile', methods=['GET'])
@verify_api_key
def profule_route():
    return "This is a protected route."