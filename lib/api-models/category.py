from typing import List, Optional
from pydantic import BaseModel
# Assuming these are in separate files in your project
# from lib.api-models.api_brand import GetBrand
# from lib.api-models.api_product_image import ProductImage

class Category(BaseModel):
    id: str
    parent_id: Optional[str] = None # Handles nulls if no parent
    name: str
    slug: str
    sub_categories: List[str]