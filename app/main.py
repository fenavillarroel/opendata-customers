from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.v1.router.user_router import router as user_router
from app.v1.router.tarifa_router import router as tarifa_router
from app.v1.router.account_router import router as account_router
from app.v1.router.cdr_router import router as cdr_router
from app.v1.router.invoice_router import router as invoice_router
from app.v1.router.payment_router import router as payment_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_router)
app.include_router(tarifa_router)
app.include_router(account_router)
app.include_router(cdr_router)
app.include_router(invoice_router)
app.include_router(payment_router)