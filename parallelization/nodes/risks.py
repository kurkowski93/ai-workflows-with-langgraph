"""
Risk Assessment Pipeline

This module implements the risk analysis track of the legal document analyzer.
It evaluates liability exposures, termination conditions, warranty limitations,
and force majeure provisions, culminating in a quantified risk assessment score.
"""

from parallelization.state import LegalDocumentAnalyzerState
from pydantic import BaseModel, Field
from parallelization.prompts import (
    LIABILITY_RISKS_TEMPLATE,
    TERMINATION_CONDITIONS_TEMPLATE,
    WARRANTY_GAPS_TEMPLATE,
    FORCE_MAJEURE_TEMPLATE,
    RISK_SCORE_TEMPLATE,
)
from parallelization.utils import create_analysis_function, call_structured_llm


class RiskScore(BaseModel):
    """
    Structured output model for risk score calculation.

    Captures both a numerical risk assessment and explanatory context
    to ensure transparent and justifiable scoring.
    """

    score: float = Field(description="Risk score from 0-100, where 100 is highest risk")
    explanation: str = Field(description="Brief explanation of the risk score")


# Liability analysis processor
analyze_liability_risks = create_analysis_function(
    LIABILITY_RISKS_TEMPLATE, "liability_risks"
)

# Termination conditions analysis processor
analyze_termination_conditions = create_analysis_function(
    TERMINATION_CONDITIONS_TEMPLATE, "termination_conditions"
)

# Warranty analysis processor
analyze_warranty_gaps = create_analysis_function(
    WARRANTY_GAPS_TEMPLATE, "warranty_gaps"
)

# Force majeure analysis processor
analyze_force_majeure_implications = create_analysis_function(
    FORCE_MAJEURE_TEMPLATE, "force_majeure_implications"
)


def calculate_risk_score(state: LegalDocumentAnalyzerState):
    """
    Calculate a comprehensive risk score based on multiple risk dimensions.

    This function aggregates findings from the various risk analysis processors
    and synthesizes them into a single, quantified risk assessment score.

    Args:
        state: The current workflow state containing risk analysis results

    Returns:
        dict: Updated state with the calculated risk score
    """
    # Prepare state with default values for missing keys
    analysis_state = {
        "document_type": state["document_type"],
        "liability_risks": state.get("liability_risks", "Not analyzed"),
        "termination_conditions": state.get("termination_conditions", "Not analyzed"),
        "warranty_gaps": state.get("warranty_gaps", "Not analyzed"),
        "force_majeure_implications": state.get(
            "force_majeure_implications", "Not analyzed"
        ),
    }

    res = call_structured_llm(analysis_state, RISK_SCORE_TEMPLATE, RiskScore)

    return {"risk_score": res.score}
