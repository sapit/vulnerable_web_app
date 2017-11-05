from flask import Flask
from flask import  request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def parse_request():
    '''
    request can have:
    username: String
    password: String
    field: String -- raises exception if its 'fuzzed'
    age: Int
    '''
    username = "username"
    password = "password"

    data = request.args  # data is empty
    # need posted data here
    print request.args
    print request.form
    # print "field" in request.form.keys()
    if "field" in request.form.keys() and request.form['field'] == "fuzzed":
        raise Exception('Fuzzed')
    
    
    sameUsername = (request.form['username'] == username) if request.form['username'] else None

    if request.form['password']:
        # unsafe password comparison
        samePass=True
        for i in range(len(password)):
            if(request.form['password'][i] != password[i]):
                samePass=False
    
    age=None
    if request.form['age']:
        age = int(request.form['age'])
    
    return "This is the login url"

app.run()
