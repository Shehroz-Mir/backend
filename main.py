from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [Product(id=1, name="Laptop", description="A high-end laptop", price=1500.0, quantity=10),
            Product(id=2, name="Smartphone", description="A latest model smartphone", price=800.0, quantity=5),
            Product(id=3, name="Headphones", description="Noise-cancelling headphones", price=200.0, quantity=15),
            Product(id=4, name="Monitor", description="4K UHD Monitor", price=400.0, quantity=7)]

@app.get("/products")
def get_products():
    return products

@app.get("/product/{id}")
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == id:
            product[index] = updated_product
            return updated_product
    return {"error": "Product not found"}

@app.delete("/product")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            deleted_product = products.pop(index)
            return deleted_product
    return {"error": "Product not found"}