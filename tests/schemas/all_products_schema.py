from pydantic import BaseModel, ConfigDict, EmailStr, Field
from datetime import datetime
from typing import List, Optional


class Dimensions(BaseModel):
    model_config = ConfigDict(extra='forbid')

    width: float
    height: float
    depth: float

class Review(BaseModel):
    model_config = ConfigDict(extra='forbid')

    rating: int = Field(ge=0, le=5)
    comment: str
    date: datetime
    reviewerName: str
    reviewerEmail: EmailStr

class Meta(BaseModel):
    model_config = ConfigDict(extra='forbid')

    createdAt: datetime
    updatedAt: datetime
    barcode: str
    qrCode: str

class Product(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: int
    title: str
    description: str
    category: str
    price: float = Field(gt=0)
    discountPercentage: float
    rating: float = Field(ge=0, le=5)
    stock: int = Field(ge=0)

    tags: List[str]
    brand: str | None = None
    sku: str
    weight: float

    dimensions: Dimensions

    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str

    reviews: List[Review]

    returnPolicy: str
    minimumOrderQuantity: int = Field(ge=1)

    meta: Meta

    thumbnail: str
    images: List[str]


class AllProductsResponse(BaseModel):
    model_config = ConfigDict(extra='forbid')

    products: List[Product]
    total: int = Field(ge=0)
    skip: int = Field(ge=0)
    limit: int = Field(gt=0)
