from pydantic import BaseModel

class marks(BaseModel):
    english_mark: int
    hindi_mark: int
    science_mark: int
    maths_mark: int
    sst_mark: int


