from flask_restx import Api, Resource, fields
import app


# confugure swagger UI
api=Api(app,title="Baby Weight Prediction API", description="An API to predict baby weight based on various maternal factors.", doc="/docs")
# create nemespace
hellow_ns=api.namespace("Hello", description="Hello World Namespace",path="/hello")
user_ns=api.namespace("User", description="User related operations", path="/user")
pread_ns=api.namespace("prediction",description="this is the prediction api where you cna predict the babdy weight based on mother parameters", path="/predict")

input_model= pread_ns.model('BabyData',{
    'gestation': fields.Float(required=True, description='Gestation period in days'),
    'parity': fields.Float(required=True, description='Number of previous pregnancies'),
    'age': fields.Float(required=True, description='Age of the mother'),
    'height': fields.Float(required=True, description='Height of the mother in inches'),
    'weight': fields.Float(required=True, description='Weight of the mother in pounds'),
    'smoke': fields.Float(required=True, description='Smoking status (0 for non-smoker, 1 for smoker)')
})

# create class for name space 
@hellow_ns.route("/")
class HelloWorld(Resource):
    def get(self):
        return "Hello, World!"

# user class 
@user_ns.route("/")
class UserCRUD(Resource):
    def get(self):
        return "User GET request"
    def post(self):
        return "User POST request"
    def put(self):
        return "User PUT request"
    def delete(self):
        return "User DELETE request"
    ""

@pread_ns.route("/")
class BabyWeightPrediction(Resource):
    @pread_ns.expect(input_model)
    def post(self):
        """"Endpoint to predict baby weight based on maternal data"""
        baby_data=request.get_json()
        # convert innto the dataframe
        # cleaned_data=get_cleaned_data(baby_data)
        df=pd.DataFrame(baby_data, index=[0])
         # select the required columns
        df=df[['gestation','parity','age','height','weight','smoke']]
        # load a machine learning model
        path=os.path.join(os.path.dirname(__file__),'model/lr.pkl')
        with open(path, 'rb') as obj:
            model=pickle.load(obj)

        # make a prediction
        prediction=model.predict(df)
        prediction=round(float(prediction[0]),2 )
        return {'predicted_weight': prediction}