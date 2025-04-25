from typing import List, Optional, Dict, TypedDict


class ProductDescriptionGeneratorState(TypedDict, total=False):
    # inputs
    product_id: str  # The id of the product

    # response from mocked database
    product_name: Optional[str]  # The name of the product
    product_image_url: Optional[str]  # The image url of the product
    product_features: Optional[List[str]]  # The features of the product
    product_category: Optional[str]  # The category of the product
    product_specifications: Optional[Dict]  # Technical specifications of the product

    # outputs
    product_features_from_image: Optional[
        str
    ]  # The description of the product from the image
    product_description: Optional[str]  # The main description of the product
    product_short_description: Optional[str]  # Short summary for product listings
    product_seo_title: Optional[str]  # SEO optimized title for the product page
    product_seo_description: Optional[str]  # SEO optimized meta description
    product_keywords: Optional[List[str]]  # Keywords for SEO purposes
