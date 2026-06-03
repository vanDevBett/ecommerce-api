def test_create_order(client, normal_user, admin_user):
    client.post("/products/",
        json={"name": "Laptop", "price": 999.99, "stock": 10},
        headers={"Authorization": f"Bearer {admin_user}"}
    )
    response = client.post("/orders/",
        json={"items": [{"product_id": 1, "quantity": 2}]},
        headers={"Authorization": f"Bearer {normal_user}"}
    )
    assert response.status_code == 201
    assert response.json()["total"] == 1999.98


def test_create_order_no_token(client):
    response = client.post("/orders/",
        json={"items": [{"product_id": 1, "quantity": 1}]}
    )
    assert response.status_code == 401


def test_create_order_insufficient_stock(client, normal_user, admin_user):
    client.post("/products/",
        json={"name": "Tablet", "price": 299.99, "stock": 1},
        headers={"Authorization": f"Bearer {admin_user}"}
    )
    response = client.post("/orders/",
        json={"items": [{"product_id": 1, "quantity": 99}]},
        headers={"Authorization": f"Bearer {normal_user}"}
    )
    assert response.status_code == 400


def test_get_orders(client, normal_user, admin_user):
    client.post("/products/",
        json={"name": "Mouse", "price": 29.99, "stock": 10},
        headers={"Authorization": f"Bearer {admin_user}"}
    )
    client.post("/orders/",
        json={"items": [{"product_id": 1, "quantity": 1}]},
        headers={"Authorization": f"Bearer {normal_user}"}
    )
    response = client.get("/orders/",
        headers={"Authorization": f"Bearer {normal_user}"}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1