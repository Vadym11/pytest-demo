from pydantic import BaseModel

class Brand(BaseModel):
    name: str
    slug: str

class GetBrand(Brand):
    id: str
