from http.client import HTTPException

from fastapi import APIRouter
from pydantic.error_wrappers import ErrorWrapper

from app.db import fake_db
from app.model import cat_details

router = APIRouter(prefix="/cat_details")


@router.get("/{cat_details_id}", response_model=cat_details.Cat_Details)
async def fetch_cat_details(cat_details_id: int):
    return fake_db.cats[cat_details_id]


@router.put("/{cat_details_id}", response_model=cat_details.Cat_Details)
async def update_item(cat_details_id: int, cat_details: cat_details.Cat_Details):
    try:
        fake_db.cats.update({cat_details_id: cat_details})
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=[ErrorWrapper(e, ("body", cat_details_id))],
            body=cat_details,
        )
    finally:
        print(fake_db.cats)
    return cat_details
