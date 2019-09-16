from typing import Tuple

from flask import Flask, jsonify, request, Response
import mockdb.mockdb_interface as db

app = Flask(__name__)


def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:
    """Wraps response in a consistent format throughout the API.

    Format inspired by https://medium.com/@shazow/how-i-design-json-api-responses-71900f00f2db
    Modifications included:
    - make success a boolean since there's only 2 values
    - make message a single string since we will only use one message per response
    IMPORTANT: data must be a dictionary where:
    - the key is the name of the type of data
    - the value is the data itself

    :param data <str> optional data
    :param status <int> optional status code, defaults to 200
    :param message <str> optional message
    :returns tuple of Flask Response and int, which is what flask expects for a response
    """
    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary 😞")

    response = {
        "code": status,
        "success": 200 <= status < 300,
        "message": message,
        "result": data,
    }
    return jsonify(response), status


"""
~~~~~~~~~~~~ API ~~~~~~~~~~~~
"""


@app.route("/")
def hello_world():
    return create_response({"content": "hello world!"})


@app.route("/mirror/<name>")
def mirror(name):
    data = {"name": name}
    return create_response(data)

@app.route("/contacts", methods=['GET'])
def get_all_contacts():
    return create_response({"contacts": db.get('contacts')})

@app.route("/shows/<id>", methods=['DELETE'])
def delete_show(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")
    db.deleteById('contacts', int(id))
    return create_response(message="Contact deleted")


# TODO: Implement the rest of the API here!
# Part 2
app.route("/contacts/<id>", methods=['GET'])
def get_contact(id):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")

    data = {"id": id}
    return create_response({"contacts": db.getById('contacts', int(id))})

# Part 4
@app.route("/contacts", methods=['POST'])
def add_contact(name, nickname, hobby):
    if name is None or nickname is None or hobby is None:
        return create_response(status=422, message="Must have valid inputs")
    data = {"name": name, "nickname": nickname, "hobby": hobby}
    db.create('contacts', data)
    return create_response(status=201)
# Part 5
app.route("/contacts/<id>", methods=['PUT'])
def update_contact(id, name, hobby):
    if db.getById('contacts', int(id)) is None:
        return create_response(status=404, message="No contact with this id exists")

    if name is None and hobby is None:
        return create_response(status=201)
    elif name is not None and hobby is not None:
        data = {"name": name, "hobby": hobby}
    elif name is not None:
        data = {"name": name}

    #hobby is not None      
    else
        data = {"hobby": hobby}

    db.updateById('contacts', int(id), data)
    return create_response(status-201)


"""
~~~~~~~~~~~~ END API ~~~~~~~~~~~~
"""
if __name__ == "__main__":
    app.run(port=8080, debug=True)
