from __init__ import app 
from route import my_routes 

app.register_blueprint(my_routes)



if __name__ == '__main__':
    app.run(debug=True)
    