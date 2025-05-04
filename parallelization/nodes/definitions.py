"""
Terminology Analysis Pipeline

This module implements the definition analysis track of the legal document analyzer.
It extracts and analyzes defined terms, industry-specific terminology, and evaluates
the consistency of term usage throughout the document.
"""

from parallelization.state import LegalDocumentAnalyzerState
from pydantic import BaseModel, Field
from typing import Dict, List
from parallelization.prompts import (
    DEFINED_TERMS_TEMPLATE,
    DEFINITION_CONSISTENCY_TEMPLATE,
)
from parallelization.utils import (
    call_llm_with_template,
    call_structured_llm,
)


class DefinedTerms(BaseModel):
    """
    Structured output model for defined terminology extraction.

    Separates terms into industry-standard and contract-specific categories
    to enable comprehensive analysis of definition usage and consistency.
    """

    industry_specific_terms: str = Field(
        description="Industry-specific terms and their definitions"
    )
    contract_specific_definitions: str = Field(
        description="Contract-specific terms and their definitions"
    )


def extract_defined_terms(state: LegalDocumentAnalyzerState):
    """
    Extract and categorize defined terminology from the legal document.

    This function identifies both explicitly defined terms within the document
    and industry-standard terminology that may be implicitly used or referenced.

    Args:
        state: The current workflow state containing document content

    Returns:
        dict: Updated state with extracted terminology categorized by type
    """
    prompt_template = DEFINED_TERMS_TEMPLATE.format(
        document_type=state["document_type"], document_text=state["document_text"]
    )

    res = call_structured_llm(state, prompt_template, DefinedTerms)

    return {
        "industry_specific_terms": res.industry_specific_terms,
        "contract_specific_definitions": res.contract_specific_definitions,
    }


def analyze_definition_consistency(state: LegalDocumentAnalyzerState):
    """
    Evaluate the consistency of terminology usage throughout the document.

    This function analyzes how consistently defined terms are used,
    identifying instances where terms may be used ambiguously, redefined,
    or employed inconsistently in different sections.

    Args:
        state: The current workflow state containing document content and extracted terms

    Returns:
        dict: Updated state with analysis of definition consistency issues
    """
    # Construct text representation of defined terms
    terms_text = ""
    if state.get("industry_specific_terms"):
        terms_text += (
            f"Industry-specific terms:\n{state['industry_specific_terms']}\n\n"
        )
    if state.get("contract_specific_definitions"):
        terms_text += (
            f"Contract-specific definitions:\n{state['contract_specific_definitions']}"
        )

    # Create a new state dictionary with terms_text for template formatting
    analysis_state = {
        "document_type": state["document_type"],
        "document_text": state["document_text"],
        "terms_text": terms_text,
    }

    result = call_llm_with_template(analysis_state, DEFINITION_CONSISTENCY_TEMPLATE)

    return {"definition_consistency_issues": result}
