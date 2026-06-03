def test_get_products_public(client):
    response = client.get("/products/")
    assert response.status_code == 200


def test_create_product_no_token(client):
    response = client.post("/products/", json={
        "name": "Laptop",
        "price": 999.99,
        "stock": 10
    })
    assert response.status_code == 401


def test_create_product_not_admin(client, normal_user):
    response = client.post("/products/",
        json={"name": "Laptop", "price": 999.99, "stock": 10},
        headers={"Authorization": f"Bearer {normal_user}"}
    )
    assert response.status_code == 403


def test_create_product_admin(client, admin_user):
    response = client.post("/products/",
        json={"name": "Laptop", "price": 999.99, "stock": 10},
        headers={"Authorization": f"Bearer {admin_user}"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Laptop"


def test_get_product(client, admin_user):
    created = client.post("/products/",
        json={"name": "Phone", "price": 499.99, "stock": 5},
        headers={"Authorization": f"Bearer {admin_user}"}
    )
    product_id = created.json()["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id


def test_get_product_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404