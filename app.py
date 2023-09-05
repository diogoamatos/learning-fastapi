import uvicorn
from fastapi import FastAPI

from routes import users, items

app = FastAPI()
app.include_router(users.users_router, prefix="/users", tags=["users"])
app.include_router(items.items_router, prefix="/items", tags=["items"])
# app.include_router(routes.modelnname_router, prefix="/models", tags=["models"])
# app.include_router(routes.path_param_router, prefix="/files", tags=["files"])


@app.get("/", tags=['index'])
def root():
    return {'data': 'hello'}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
