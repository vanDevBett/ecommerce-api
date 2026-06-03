from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.products import router as products_router
from app.api.orders import router as orders_router
from app.core.database import Base, engine
from app.core.exceptions import add_exception_handlers

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce API",
    description="REST API for e-commerce with JWT authentication and role-based access",
    version="1.0.0"
)

add_exception_handlers(app)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(products_router, prefix="/products", tags=["products"])
app.include_router(orders_router, prefix="/orders", tags=["orders"])


@app.get("/")
def root():
    return {"message": "E-commerce API is running"}