from prompt_chaining.state import ProductDescriptionGeneratorState
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
    mock_data_path = os.path.join(current_dir, ".", "mock_data", "mock_data.json")

    with open(mock_data_path, "r") as file:
        products = json.load(file)

    # Find product by ID
    product = next(
        (p for p in products if p["product_id"] == state["product_id"]), None
    )

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
    if state["product_name"] is None:
        print("Product not found")
        return "END"
    else:
        return "analyze_product_image"


def extract_product_features_from_image(state: ProductDescriptionGeneratorState):

    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

    res = llm.invoke(
        [
            HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": f"""
                            Analyze the product image and extract key visual features.
                            Return a concise, bullet-point list of observable product attributes and characteristics.
                            Focus on physical appearance, visible features, and distinguishing elements.
                            Ensure the extracted information is factual and directly observable in the image.
                            """,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": state["product_image_url"]},
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
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3)

    prompt = f"""
    PRODUCT INFORMATION:
    Name: {state["product_name"]}
    Features: {state["product_features"]}
    Category: {state["product_category"]}
    Specifications: {state["product_specifications"]}
    Visual Features: {state["product_features_from_image"]}
    
    TASK:
    Create a comprehensive product description that effectively communicates value to potential customers.
    
    REQUIREMENTS:
    - Length: 100-150 words
    - Tone: Professional and informative
    - Structure: Introduction, key features, benefits, conclusion
    - SEO: Incorporate relevant keywords naturally
    - Include important technical specifications where relevant
    - Highlight unique selling points and competitive advantages
    
    PRODUCT DESCRIPTION:
    """

    res = llm.invoke(prompt)

    return {"product_description": res.content}


def generate_product_short_description(state: ProductDescriptionGeneratorState):
    """
    Generate a short description for the product.
    """
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

    prompt = f"""
    PRODUCT INFORMATION:
    Name: {state["product_name"]}
    Full Description: {state["product_description"]}
    
    TASK:
    Create a concise product summary for use in listings, search results, and catalog entries.
    
    REQUIREMENTS:
    - Length: 15-25 words
    - Tone: Compelling and informative
    - Must capture the product's core value proposition
    - Include primary keywords without keyword stuffing
    - Suitable for display in search results and product cards
    
    SHORT DESCRIPTION:
    """

    res = llm.invoke(prompt)

    return {"product_short_description": res.content}


def generate_product_seo_title(state: ProductDescriptionGeneratorState):
    """
    Generate a SEO title for the product.
    """
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

    prompt = f"""
    PRODUCT INFORMATION:
    Name: {state["product_name"]}
    Description: {state["product_description"]}
    
    TASK:
    Create an SEO-optimized title for the product page.
    
    REQUIREMENTS:
    - Length: 50-60 characters maximum
    - Must include the product name
    - Include a primary keyword near the beginning
    - Communicate unique selling point if possible
    - Avoid keyword stuffing or unnatural phrasing
    - Compelling for users but optimized for search engines
    
    SEO TITLE:
    """

    res = llm.invoke(prompt)

    return {"product_seo_title": res.content}


def generate_product_seo_description(state: ProductDescriptionGeneratorState):
    """
    Generate a SEO description for the product.
    """
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

    prompt = f"""
    PRODUCT INFORMATION:
    Name: {state["product_name"]}
    Description: {state["product_description"]}
    
    TASK:
    Create an SEO-optimized meta description for the product page.
    
    REQUIREMENTS:
    - Length: 150-160 characters maximum
    - Include the primary keyword and at least one secondary keyword
    - Communicate unique value proposition
    - Include a clear call-to-action
    - Must be compelling for users to click through from search results
    - Avoid truncation in search results by staying within character limits
    
    SEO META DESCRIPTION:
    """

    res = llm.invoke(prompt)

    return {"product_seo_description": res.content}


def generate_product_keywords(state: ProductDescriptionGeneratorState):
    """
    Generate a list of keywords for the product.
    """
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

    prompt = f"""
    PRODUCT INFORMATION:
    Name: {state["product_name"]}
    Description: {state["product_description"]}
    
    TASey:
    Generate a structured list of SEO ywrdywords for the product.
    
    REQUIREMENTS:
    - Include 10-15 relevant keywords and phrases
    - Categorize by:
      * Primary keywords (2-3)
      * Secondary keywords (4-5)
      * Long-tail keywords (4-7)
    - Include a mix of commercial and informational intent keywords
    - Consider search volume and competition (prioritize attainable keywords)
    - Format the results as a structured list grouped by category
    
    KEYWORDS:
    """

    res = llm.invoke(prompt)

    return {"product_keywords": res.content}
