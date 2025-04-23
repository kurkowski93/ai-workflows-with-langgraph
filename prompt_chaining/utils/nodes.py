from prompt_chaining.utils.state import ProductDescriptionGeneratorState
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import json
import os


def find_product_details(state: ProductDescriptionGeneratorState):
    """
    Find details about the product using the product ID.
    """
    # Load mock data
    current_dir = os.path.dirname(os.path.abspath(__file__))
    mock_data_path = os.path.join(current_dir, "..", "mock_data", "mock_data.json")

    with open(mock_data_path, "r") as file:
        products = json.load(file)

    # Find product by ID
    product = next((p for p in products if p["product_id"] == state.product_id), None)

    if product:
        return {
            "product_name": product["product_name"],
            "product_image_url": product["product_image_url"],
            "product_features": product["product_features"],
            "product_category": product["product_category"],
            "product_specifications": product["product_specifications"],
        }
    else:
        return {}


def gate_product_found(state: ProductDescriptionGeneratorState):
    """
    Gate the product details to ensure they are valid.
    """
    if state.product_name is None:
        print("Product not found")
        return "END"
    else:
        return "analyze_product_image"


def extract_product_features_from_image(state: ProductDescriptionGeneratorState):

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    res = llm.invoke(
        [
            HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": f"""
                            Extract key features from the image of the product. 
                            Extracted informations should be in bullet points and will be used to generate a description for the product.
                            """,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": state.product_image_url},
                    },
                ]
            )
        ]
    )

    return {"product_features_from_image": res.content}


def generate_product_description(state: ProductDescriptionGeneratorState):
    """
    Generate a description for the product.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    prompt = f"""
    
    Based on the following product details, generate a description for the product:
    
    Product Name: {state.product_name}
    Product Features: {state.product_features}
    Product Category: {state.product_category}
    Product Specificaiton: {state.product_specifications}
    Product Features from Image: {state.product_features_from_image}
    
    Use this guidelines to generate the description:
    
    - The description should be SEO friendly
    - The description should be 100-150 words
    - The description should be written in a way that is easy to understand
    
    Product description:
    """

    res = llm.invoke(prompt)

    return {"product_description": res.content}


def generate_product_short_description(state: ProductDescriptionGeneratorState):
    """
    Generate a short description for the product.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
    
    Based on the following product details, generate a short description for the product:
    
    Product Name: {state.product_name}
    Product Description: {state.product_description}
    
    Short description:
    """

    res = llm.invoke(prompt)

    return {"product_short_description": res.content}


def generate_product_seo_title(state: ProductDescriptionGeneratorState):
    """
    Generate a SEO title for the product.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
    
    Based on the following product details, generate a SEO title for the product:
    
    Product Name: {state.product_name}
    
    Product seo title:
    """

    res = llm.invoke(prompt)

    return {"product_seo_title": res.content}


def generate_product_seo_description(state: ProductDescriptionGeneratorState):
    """
    Generate a SEO description for the product.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
    
    Based on the following product details, generate a SEO description for the product:
    
    Product Name: {state.product_name}
    Product Description: {state.product_description}
    """

    res = llm.invoke(prompt)

    return {"product_seo_description": res.content}


def generate_product_keywords(state: ProductDescriptionGeneratorState):
    """
    Generate a list of keywords for the product.
    """
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    prompt = f"""
    
    Based on the following product details, generate a list of keywords for the product:
    
    Product Name: {state.product_name}
    Product Description: {state.product_description}
    
    Product keywords:
    """

    res = llm.invoke(prompt)

    return {"product_keywords": res.content}
