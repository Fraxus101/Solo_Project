from flask_app import app
from flask_app.controllers import Posts, Users



if __name__ == "__main__":
    app.run(debug=True , port=5002)