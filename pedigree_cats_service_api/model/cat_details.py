from typing import Optional

from pydantic import BaseModel, Field, validator
from datetime import date


class Cat_Details(BaseModel):
    cat_details_id: int = Field(example="1")
    name: str = Field(example="Dumpling")
    coat_colour: str = Field(example="Black")
    coat_type: str = Field(example="Curly")
    dob: date = Field(example="2014-06-21")
    gems_code: Optional[str] = Field(example="SRLd03")

    @validator("gems_code")
    def validate_gems_code(cls, v) -> str:
        if v and len(v) < 4:
            raise ValueError(
                f"Invalid gems_code: {v}\nPlease go to https://www.gccfcats.org/wp-content/uploads/2022/01/GEMS-Codes.9Nov21.pdf for more information"
            )
        return v
