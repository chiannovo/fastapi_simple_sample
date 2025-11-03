'''
Author: ChiaEnKang
Date: 2025-11-03 11:07:30
LastEditors: ChiaEnKang
LastEditTime: 2025-11-03 11:10:18
'''
from fastapi import APIRouter


router = APIRouter()


@router.get("/list")
def read_users():

    return {"message": "List users"}

