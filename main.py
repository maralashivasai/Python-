from flask import Flask,jsonify

app =Flask(__name__)
items=[{"name":"apple",
        "price":130,
        'item_id':0},
       {"name":"banana",
               "price":70,
                       'item_id': 1}]


@app.route('/')
def index():
    return "welcome to my firs api"
@app.route("/items",methods=['GET'])
def get():
    return jsonify({'items':items})

@app.route("/items/<int:item_idn>",methods=['GET'])
def get_id(item_idn):
    return jsonify({"item":items[item_idn]})

@app.route("/itemsc",methods=['POST'])
def postitem():
    i={"name":"kiwi",
               "price":90,
                       'item_id': 2}
    items.append(i)
    return jsonify({"added":i})


@app.route("/items/<int:item_id>",methods=['put'])
def update(item_id):
    items[item_id]['price']=567
    return jsonify({"item":items[item_id]})

@app.route("/items/<int:item_id>",methods=['delete'])
def delete(item_id):
    items.remove(items[item_id])
    return jsonify({"result":True})




if __name__=="__main__":
    app.run(debug=True)