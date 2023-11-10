#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
-Your web application must be listening on 0.0.0.0, port 5000
-You must use storage for fetching data from the storage engine (FileStorage or
DBStorage) => from models import storage and storage.all(...)
-To load all cities of a State:
--If your storage engine is DBStorage, you must use cities relationship
--Otherwise, use the public getter method cities
-After each request you must remove the current SQLAlchemy Session:
--Declare a method to handle @app.teardown_appcontext
--Call in this method storage.close()
-Routes:
--/states: display a HTML page: (inside the tag BODY)
---H1 tag: “States”
---UL tag: with the list of all State objects present in DBStorage sorted by
name (A->Z) tip
----LI tag: description of one State: <state.id>: <B><state.name></B>
--/states/<id>: display a HTML page: (inside the tag BODY)
---If a State object is found with this id:
----H1 tag: “State: ”
----H3 tag: “Cities:”
----UL tag: with the list of City objects linked to the State sorted by name
(A->Z)
-----LI tag: description of one City: <city.id>: <B><city.name></B>
---Otherwise:
----H1 tag: “Not found!”
-You must use the option strict_slashes=False in your route definition
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_route(id=None):
    request = None
    states_list = storage.all('State').values()
    if id is not None:
        request = next(
            (state for state in states_list if state.id == id),
            False
        )
    return render_template(
        '9-states.html',
        request=request,
        states_list=states_list
    )


@app.teardown_appcontext
def remover(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
