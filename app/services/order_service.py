from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem
from app.models.product import Product
from app.schemas.order import OrderCreate
from fastapi import HTTPException, status


def create_order(db: Session, order: OrderCreate, user_id: int) -> Order:
    total = 0.0
    order_items = []

    for item in order.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product {item.product_id} not found"
            )
        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.name}"
            )
        total += product.price * item.quantity
        order_items.append((product, item.quantity))

    db_order = Order(user_id=user_id, total=total)
    db.add(db_order)
    db.flush()

    for product, quantity in order_items:
        db_item = OrderItem(
            order_id=db_order.id,
            product_id=product.id,
            quantity=quantity,
            unit_price=product.price
        )
        product.stock -= quantity
        db.add(db_item)

    db.commit()
    db.refresh(db_order)
    return db_order


def get_orders(db: Session, user_id: int) -> list[Order]:
    return db.query(Order).filter(Order.user_id == user_id).all()


def get_order(db: Session, order_id: int, user_id: int) -> Order | None:
    return db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user_id
    ).first()