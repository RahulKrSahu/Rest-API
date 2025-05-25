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

@app.get("/store")
def get_stores():
    return {"stores": stores}

if __name__ == '__main__':
    app.run(debug=True)