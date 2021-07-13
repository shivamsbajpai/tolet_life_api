from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .data.database import engine, Base
from .routers import rentDetailsRouter, statusRouter, identityRouter, imageRouter, userRentDetailsRouter, productCategoryRouter, userProfileDetailsRouter

tags_metadata = [
    {
        "name": "ToLet Life API",
        "externalDocs": {
            "description": "Created with love ❤️. Contact developer",
            "url": "https://tinyurl.com/3jyarv3h",
        },
    },
]

app = FastAPI(title="ToLet Life", openapi_tags=tags_metadata)
version_prefix = '/api/v1'

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(engine)

app.include_router(identityRouter.router, prefix=version_prefix)
app.include_router(imageRouter.router, prefix=version_prefix)
app.include_router(rentDetailsRouter.router, prefix=version_prefix)
app.include_router(userRentDetailsRouter.router, prefix=version_prefix)
app.include_router(userProfileDetailsRouter.router,prefix=version_prefix)
app.include_router(productCategoryRouter.router, prefix=version_prefix)
app.include_router(statusRouter.router, prefix=version_prefix)
