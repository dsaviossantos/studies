import  uuid
from    flask   import  Flask
from    flask_restful   import Api, Resource, reqparse, abort, fields, marshal_with
from    flask_sqlalchemy    import  SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost/postgres'
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(100), nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f"User(name = {name})"

db.create_all()
user_post_args = reqparse.RequestParser()
user_post_args.add_argument("email", type=str, required=True)
user_post_args.add_argument("name", type=str, required=True)
user_post_args.add_argument("location", type=dict, required=True)
user_post_args.add_argument("gender", type=str, required=True)

user_location_args = reqparse.RequestParser()
user_location_args.add_argument("address", type=str, required=True, location=('location'))
user_location_args.add_argument("district", type=str, required=True, location=('location'))
user_location_args.add_argument("city", type=str, required=True, location=('location'))
user_location_args.add_argument("state", type=str, required=True, location=('location'))
user_location_args.add_argument("country", type=str, required=True, location=('location'))
user_location_args.add_argument("zipcode", type=int, required=True, location=('location'))


resources_fields = {
    'email': fields.String,
    'name': fields.String,
    'location':fields.Nested({
        'address': fields.String,
        'district': fields.String,
        'city': fields.String,
        'state': fields.String,
        'country': fields.String,
        'zipcode': fields.Integer
    }),
    'gender': fields.String
}

class UserResouce(Resource):
    @marshal_with(resources_fields)
    def get(self, user_id):
        result = User.query.filter_by(id=user_id).all()
        return result
    
    @marshal_with(resources_fields)
    def post(self):
        user_args = user_post_args.parse_args()
        location_args = user_location_args.parse_args(req=user_args)
        user = User(
            email=user_args['email'],
            name=user_args['name'],
            address= location_args['address'],
            district=location_args['district'],
            city=location_args['city'],
            state=location_args['state'],
            country=location_args['country'],
            zipcode=location_args['zipcode'],
            gender=user_args['gender'])
        db.session.add(user)
        db.session.commit()
        return user, 201


api.add_resource(UserResouce, "/user")

if  __name__ == "__main__":
    app.run(debug=True)