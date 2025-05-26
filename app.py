import datetime
from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "DMART",
        "items": [
            {
                "name": "Detergent",
                "price": 80.5
            }
        ]
    }
]

@app.get("/store") #return all stores
def get_stores():
    sorted_stores = sorted(stores, key=lambda store: store["name"])
    return {"stores": sorted_stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return {"message": "Store created", "stores": stores}, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    for store in stores:
        if store["name"] == name:
            request_data = request.get_json()
            price = request_data["price"]
            if price <= 0:
                return {"message": "Price must be positive"}, 400
            new_item = {"name": request_data["name"], "price": price}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

@app.delete("/store/<string:name>")
def delete_store(name):
    global stores
    stores = [store for store in stores if store["name"] != name]
    return {"message": f"Store '{name}' deleted"}, 200

if __name__ == '__main__':
    app.run(debug=True)