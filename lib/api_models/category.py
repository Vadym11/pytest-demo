from typing import List, Optional
from pydantic import BaseModel

class Category(BaseModel):
    id: str
    parent_id: Optional[str] = None # Handles nulls if no parent
    name: str
    slug: str
    sub_categories: List[str]