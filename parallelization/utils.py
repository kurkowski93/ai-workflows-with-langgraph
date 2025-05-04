"""
Legal Document Analysis Utilities

This module provides core utility functions and configuration settings
for the Legal Document Analysis workflow. It contains standardized methods
for LLM interactions with consistent error handling, templating, and
structured output parsing.
"""

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from typing import Any, Dict, List, Type


class LLMConfig:
    """
    Configuration parameters for language model interactions.

    This class centralizes all model selection and generation parameters
    to ensure consistent behavior across the entire workflow.
    """

    DEFAULT_MODEL = "gpt-4.1-mini"
    DEFAULT_TEMPERATURE = 0


def call_llm_with_template(
    template_values,
    template,
    model=LLMConfig.DEFAULT_MODEL,
    temperature=LLMConfig.DEFAULT_TEMPERATURE,
):
    """
    Execute an LLM call with standardized template processing.

    This function handles the complete process of formatting a prompt template
    with state values, executing the LLM call, and extracting the response content.

    Args:
        template_values: Dictionary of values to populate the template
        template: PromptTemplate object from the prompts module
        model: LLM model identifier (defaults to configuration default)
        temperature: Sampling temperature for response generation

    Returns:
        str: The processed content from the LLM response
    """
    llm = ChatOpenAI(model=model, temperature=temperature)

    # Format the prompt template with appropriate values
    prompt = template.format(**template_values)

    res = llm.invoke(prompt)

    return res.content


def call_structured_llm(
    template_values,
    prompt_template,
    output_class,
    model=LLMConfig.DEFAULT_MODEL,
    temperature=LLMConfig.DEFAULT_TEMPERATURE,
):
    """
    Execute an LLM call with structured output validation.

    This function enables type-safe interaction with language models by
    enforcing a schema on the response through Pydantic model validation.

    Args:
        template_values: Dictionary of values to populate the template
        prompt_template: String template for the prompt
        output_class: Pydantic model class defining the expected response structure
        model: LLM model identifier (defaults to configuration default)
        temperature: Sampling temperature for response generation

    Returns:
        An instance of output_class with the structured LLM response
    """
    structured_llm = ChatOpenAI(
        model=model, temperature=temperature
    ).with_structured_output(output_class)

    # Format the prompt template with appropriate values
    prompt = prompt_template.format(**template_values)

    return structured_llm.invoke(prompt)


def create_analysis_function(template, result_key):
    """
    Factory function that creates standardized document analysis processors.

    This higher-order function generates specialized analysis functions with
    consistent error handling, state management, and output formatting. It
    enables consistent behavior across multiple analysis nodes while reducing
    code duplication.

    Args:
        template: PromptTemplate for the specific analysis task
        result_key: State dictionary key for storing the analysis result

    Returns:
        function: A state processor function compatible with LangGraph nodes
    """

    def analyze_function(state):
        result = call_llm_with_template(state, template)
        return {result_key: result}

    return analyze_function
