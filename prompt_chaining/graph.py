"""
Product Description Generator Workflow

This script defines a LangGraph workflow that takes a product ID and generates
various marketing content including product descriptions, SEO titles, and keywords.

The workflow demonstrates prompt chaining - a simple but powerful technique
where multiple LLM calls are chained together, with each step building on the results
of previous steps.
"""

import sys
import os
import argparse

from langgraph.graph import StateGraph, END, START
from prompt_chaining.state import ProductDescriptionGeneratorState
from prompt_chaining.nodes import (
    find_product_details,
    gate_product_found,
    extract_product_features_from_image,
    generate_product_description,
    generate_product_short_description,
    generate_product_seo_title,
    generate_product_seo_description,
    generate_product_keywords,
)

# Create a state graph with our state type
graph = StateGraph(ProductDescriptionGeneratorState)

# Add all the nodes to our graph
graph.add_node("find_product_details", find_product_details)
graph.add_node(
    "extract_product_features_from_image", extract_product_features_from_image
)
graph.add_node("generate_product_description", generate_product_description)
graph.add_node("generate_product_short_description", generate_product_short_description)
graph.add_node("generate_product_seo_title", generate_product_seo_title)
graph.add_node("generate_product_seo_description", generate_product_seo_description)
graph.add_node("generate_product_keywords", generate_product_keywords)

# Define the workflow by connecting the nodes
graph.add_edge(START, "find_product_details")
graph.add_conditional_edges(
    "find_product_details",
    gate_product_found,
    {"END": END, "analyze_product_image": "extract_product_features_from_image"},
)
graph.add_edge("extract_product_features_from_image", "generate_product_description")
graph.add_edge("generate_product_description", "generate_product_short_description")
graph.add_edge("generate_product_short_description", "generate_product_seo_title")
graph.add_edge("generate_product_seo_title", "generate_product_seo_description")
graph.add_edge("generate_product_seo_description", "generate_product_keywords")
graph.add_edge("generate_product_keywords", END)

# Compile the graph into a runnable
workflow = graph.compile()
