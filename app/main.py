from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .data.database import engine,Base
from .routers import rentDetailsRouter,statusRouter,identityRouter,imageRouter,userRentDetailsRouter


app = FastAPI(
    title='ToLet_Life API',
    description='Created with fastAPI',
    version='1.0.0'
)
version_prefix='/api/v1'

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(engine)

app.include_router(identityRouter.router,prefix=version_prefix)
app.include_router(imageRouter.router,prefix=version_prefix)
app.include_router(rentDetailsRouter.router,prefix=version_prefix)
app.include_router(userRentDetailsRouter.router,prefix=version_prefix)
app.include_router(statusRouter.router,prefix=version_prefix)