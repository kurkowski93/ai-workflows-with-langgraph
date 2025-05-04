"""
Strategic Opportunity Analysis Pipeline

This module implements the opportunity analysis track of the legal document analyzer.
It identifies advantageous provisions related to pricing terms, contract extensions,
service expansion options, and favorable termination conditions.
"""

from parallelization.state import LegalDocumentAnalyzerState
from pydantic import BaseModel, Field
from parallelization.prompts import (
    PRICING_LEVERAGE_POINTS_TEMPLATE,
    CONTRACT_EXTENSION_OPTIONS_TEMPLATE,
    SERVICE_SCOPE_EXPANSION_TEMPLATE,
    EARLY_TERMINATION_ADVANTAGES_TEMPLATE,
    OPPORTUNITY_SCORE_TEMPLATE,
)
from parallelization.utils import create_analysis_function, call_structured_llm


class OpportunityScore(BaseModel):
    """
    Structured output model for opportunity assessment scoring.

    Captures both a numerical opportunity assessment and explanatory context
    to ensure transparent and justifiable scoring.
    """

    score: float = Field(
        description="Opportunity score from 0-100, where 100 is highest opportunity",
    )
    explanation: str = Field(description="Brief explanation of the opportunity score")


# Pricing leverage analysis processor
analyze_pricing_leverage_points = create_analysis_function(
    PRICING_LEVERAGE_POINTS_TEMPLATE, "pricing_leverage_points"
)

# Contract extension analysis processor
analyze_contract_extension_options = create_analysis_function(
    CONTRACT_EXTENSION_OPTIONS_TEMPLATE, "contract_extension_options"
)

# Service scope analysis processor
analyze_service_scope_expansion = create_analysis_function(
    SERVICE_SCOPE_EXPANSION_TEMPLATE, "service_scope_expansion"
)

# Termination advantages analysis processor
analyze_early_termination_advantages = create_analysis_function(
    EARLY_TERMINATION_ADVANTAGES_TEMPLATE, "early_termination_advantages"
)


def calculate_opportunity_score(state: LegalDocumentAnalyzerState):
    """
    Calculate a comprehensive opportunity score based on multiple opportunity dimensions.

    This function aggregates findings from the various opportunity analysis processors
    and synthesizes them into a single, quantified opportunity assessment score.

    Args:
        state: The current workflow state containing opportunity analysis results

    Returns:
        dict: Updated state with the calculated opportunity score
    """
    # Prepare state with default values for missing keys
    analysis_state = {
        "document_type": state["document_type"],
        "pricing_leverage_points": state.get("pricing_leverage_points", "Not analyzed"),
        "contract_extension_options": state.get(
            "contract_extension_options", "Not analyzed"
        ),
        "service_scope_expansion": state.get("service_scope_expansion", "Not analyzed"),
        "early_termination_advantages": state.get(
            "early_termination_advantages", "Not analyzed"
        ),
    }

    res = call_structured_llm(
        analysis_state, OPPORTUNITY_SCORE_TEMPLATE, OpportunityScore
    )

    return {"opportunity_score": res.score}
