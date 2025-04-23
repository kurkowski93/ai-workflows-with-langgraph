from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class ProductDescriptionGeneratorState:
    # inputs
    product_id: str  # The id of the product

    # response from mocked database
    product_name: Optional[str] = None  # The name of the product
    product_image_url: Optional[str] = None  # The image url of the product
    product_features: Optional[List[str]] = None  # The features of the product
    product_category: Optional[str] = None  # The category of the product
    product_specifications: Optional[Dict] = (
        None  # Technical specifications of the product
    )
    product_features_from_image: Optional[str] = (
        None  # The description of the product from the image
    )

    # outputs
    product_description: Optional[str] = None  # The main description of the product
    product_short_description: Optional[str] = (
        None  # Short summary for product listings
    )
    product_seo_title: Optional[str] = None  # SEO optimized title for the product page
    product_seo_description: Optional[str] = None  # SEO optimized meta description
    product_keywords: Optional[List[str]] = None  # Keywords for SEO purposes
    product_benefits: Optional[List[str]] = None  # Key benefits of using this product
    product_use_cases: Optional[List[str]] = None  # Common use cases for the product
