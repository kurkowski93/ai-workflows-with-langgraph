"""
Cross-Reference Validation Pipeline

This module implements the cross-reference analysis track of the legal document analyzer.
It identifies inconsistencies, contradictions, and logical conflicts between different
sections of the document to ensure legal coherence and enforceability.
"""

from parallelization.state import LegalDocumentAnalyzerState
from parallelization.prompts import (
    DIRECT_CONTRADICTIONS_TEMPLATE,
    IMPLIED_INCONSISTENCIES_TEMPLATE,
    SEQUENTIAL_COMMITMENT_ISSUES_TEMPLATE,
)
from parallelization.utils import call_llm_with_template


def identify_direct_contradictions(state: LegalDocumentAnalyzerState):
    """
    Detect explicit contradictions between different clauses in the document.

    This function analyzes the document to find instances where provisions
    directly contradict each other, creating potential legal ambiguities.

    Args:
        state: The current workflow state containing document content

    Returns:
        dict: Updated state with identified contradictions
    """
    result = call_llm_with_template(state, DIRECT_CONTRADICTIONS_TEMPLATE)

    return {"direct_contradictions": result}


def identify_implied_inconsistencies(state: LegalDocumentAnalyzerState):
    """
    Detect logical inconsistencies that create indirect conflicts.

    This function analyzes provisions that, while not directly contradictory,
    create logical conflicts when interpreted together in the full context.

    Args:
        state: The current workflow state containing document content

    Returns:
        dict: Updated state with identified logical inconsistencies
    """
    result = call_llm_with_template(state, IMPLIED_INCONSISTENCIES_TEMPLATE)

    return {"implied_inconsistencies": result}


def identify_sequential_commitment_issues(state: LegalDocumentAnalyzerState):
    """
    Identify timeline conflicts and sequential dependency problems.

    This function analyzes the temporal aspects of commitments to detect
    issues with sequencing, deadlines, and prerequisite conditions.

    Args:
        state: The current workflow state containing document content

    Returns:
        dict: Updated state with identified sequential commitment issues
    """
    result = call_llm_with_template(state, SEQUENTIAL_COMMITMENT_ISSUES_TEMPLATE)

    return {"sequential_commitment_issues": result}
