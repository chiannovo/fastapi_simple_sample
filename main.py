'''
Author: ChiaEnKang
Date: 2025-11-03 11:06:17
LastEditors: ChiaEnKang
LastEditTime: 2025-11-03 11:06:48
'''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/api/users")

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8181, reload=False)
