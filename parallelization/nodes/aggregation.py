"""
Analysis Aggregation and Reporting Module

This module implements the final stage of the legal document analysis workflow,
consolidating results from all parallel processing tracks into cohesive insights
and generating comprehensive reports with actionable recommendations.
"""

from parallelization.state import LegalDocumentAnalyzerState
from pydantic import BaseModel, Field
from typing import List, Optional
from parallelization.utils import call_structured_llm, LLMConfig
from parallelization.prompts import (
    KEY_INSIGHTS_TEMPLATE,
    CRITICAL_ISSUES_TEMPLATE,
    MARKDOWN_REPORT_TEMPLATE,
)


class KeyInsights(BaseModel):
    """
    Structured output model for key document insights.

    Captures the most significant findings from across all analysis dimensions
    in a format suitable for executive summaries and high-level reporting.
    """

    key_insights: List[str] = Field(
        description="List of key insights from the document analysis"
    )


class CriticalIssues(BaseModel):
    """
    Structured output model for critical document issues.

    Identifies high-priority concerns that require immediate attention
    or present significant legal, operational, or financial risks.
    """

    critical_issues: List[str] = Field(
        description="List of critical issues requiring immediate attention"
    )


class MarkdownReport(BaseModel):
    """
    Structured output model for the comprehensive analysis report.

    Provides a complete, formatted report suitable for stakeholder review,
    including executive summary, detailed findings, and recommendations.
    """

    markdown_report: str = Field(
        description="Complete markdown report summarizing the legal document analysis"
    )


def aggregate_key_insights(state: LegalDocumentAnalyzerState):
    """
    Synthesize key insights from all parallel analysis tracks.

    This function consolidates findings across all document analysis dimensions,
    identifying the most significant patterns, opportunities, and risks to create
    a prioritized list of insights for stakeholders.

    Args:
        state: The current workflow state containing all analysis results

    Returns:
        dict: Updated state with aggregated key insights
    """
    # Prepare a consolidated summary of all analyses
    analyses = []
    if state.get("document_summary"):
        analyses.append(f"DOCUMENT SUMMARY:\n{state['document_summary']}")

    # Add obligation analyses
    for field in [
        "payment_obligations",
        "delivery_timelines",
        "reporting_requirements",
        "performance_criteria",
    ]:
        if state.get(field):
            analyses.append(f"{field.upper().replace('_', ' ')}:\n{state[field]}")

    # Add risk analyses
    for field in [
        "liability_risks",
        "termination_conditions",
        "warranty_gaps",
        "force_majeure_implications",
    ]:
        if state.get(field):
            analyses.append(f"{field.upper().replace('_', ' ')}:\n{state[field]}")

    # Add opportunity analyses
    for field in [
        "pricing_leverage_points",
        "contract_extension_options",
        "service_scope_expansion",
        "early_termination_advantages",
    ]:
        if state.get(field):
            analyses.append(f"{field.upper().replace('_', ' ')}:\n{state[field]}")

    # Add definition issues - now as raw string
    if state.get("definition_consistency_issues"):
        analyses.append(
            f"DEFINITION CONSISTENCY ISSUES:\n{state['definition_consistency_issues']}"
        )

    # Add cross-reference issues - now as raw strings
    for field in [
        "direct_contradictions",
        "implied_inconsistencies",
        "sequential_commitment_issues",
    ]:
        if state.get(field):
            analyses.append(f"{field.upper().replace('_', ' ')}:\n{state[field]}")

    # Add scores if available
    if state.get("risk_score") is not None:
        analyses.append(f"RISK SCORE: {state['risk_score']}/100")
    if state.get("opportunity_score") is not None:
        analyses.append(f"OPPORTUNITY SCORE: {state['opportunity_score']}/100")

    analyses_text = "\n\n".join(analyses)

    # Prepare state for structured LLM
    analysis_state = {
        "document_type": state["document_type"],
        "analyses_text": analyses_text,
    }

    res = call_structured_llm(analysis_state, KEY_INSIGHTS_TEMPLATE, KeyInsights)

    return {"key_insights": res.key_insights}


def identify_critical_issues(state: LegalDocumentAnalyzerState):
    """
    Identify high-priority issues requiring immediate attention.

    This function evaluates all identified risks and inconsistencies to determine
    which issues present the most significant concerns based on potential impact,
    probability, and urgency.

    Args:
        state: The current workflow state containing all analysis results

    Returns:
        dict: Updated state with prioritized critical issues
    """
    # Consolidate issues across all analyses
    issues = []

    # Add risks
    for field in [
        "liability_risks",
        "termination_conditions",
        "warranty_gaps",
        "force_majeure_implications",
    ]:
        if state.get(field):
            issues.append(f"{field.upper().replace('_', ' ')}:\n{state[field]}")

    # Add definition issues - now as raw string
    if state.get("definition_consistency_issues"):
        issues.append(
            f"DEFINITION CONSISTENCY ISSUES:\n{state['definition_consistency_issues']}"
        )

    # Add cross-reference issues - now as raw strings
    for field in [
        "direct_contradictions",
        "implied_inconsistencies",
        "sequential_commitment_issues",
    ]:
        if state.get(field):
            issues.append(f"{field.upper().replace('_', ' ')}:\n{state[field]}")

    issues_text = "\n\n".join(issues)
    risk_score = state.get("risk_score", "Not calculated")

    # Prepare state for structured LLM
    analysis_state = {
        "document_type": state["document_type"],
        "issues_text": issues_text,
        "risk_score": risk_score,
    }

    res = call_structured_llm(analysis_state, CRITICAL_ISSUES_TEMPLATE, CriticalIssues)

    return {"critical_issues": res.critical_issues}


def generate_markdown_report(state: LegalDocumentAnalyzerState):
    """
    Generate a comprehensive, structured report of the complete analysis.

    This function compiles all analysis results into a professionally formatted
    markdown document suitable for stakeholder review, including executive summary,
    detailed findings by category, and actionable recommendations.

    Args:
        state: The current workflow state containing all analysis results

    Returns:
        dict: Updated state with the complete markdown report
    """
    # Use the state directly without creating intermediate variables
    # Add default values for missing fields directly in the state dictionary
    report_state = {
        # Input fields - required
        "document_type": state["document_type"],
        # Use get() with defaults for all optional fields
        "document_summary": state.get("document_summary", "No summary available"),
        "risk_score": state.get("risk_score", "Not calculated"),
        "opportunity_score": state.get("opportunity_score", "Not calculated"),
        # Obligation analyses
        "payment_obligations": state.get("payment_obligations", "Not analyzed"),
        "delivery_timelines": state.get("delivery_timelines", "Not analyzed"),
        "reporting_requirements": state.get("reporting_requirements", "Not analyzed"),
        "performance_criteria": state.get("performance_criteria", "Not analyzed"),
        # Risk analyses
        "liability_risks": state.get("liability_risks", "Not analyzed"),
        "termination_conditions": state.get("termination_conditions", "Not analyzed"),
        "warranty_gaps": state.get("warranty_gaps", "Not analyzed"),
        "force_majeure_implications": state.get(
            "force_majeure_implications", "Not analyzed"
        ),
        # Opportunity analyses
        "pricing_leverage_points": state.get("pricing_leverage_points", "Not analyzed"),
        "contract_extension_options": state.get(
            "contract_extension_options", "Not analyzed"
        ),
        "service_scope_expansion": state.get("service_scope_expansion", "Not analyzed"),
        "early_termination_advantages": state.get(
            "early_termination_advantages", "Not analyzed"
        ),
        # Definition analyses
        "industry_specific_terms": state.get(
            "industry_specific_terms", "None identified"
        ),
        "contract_specific_definitions": state.get(
            "contract_specific_definitions", "None identified"
        ),
        "definition_consistency_issues": state.get(
            "definition_consistency_issues", "None identified"
        ),
        # Cross-reference analyses
        "direct_contradictions": state.get("direct_contradictions", "None identified"),
        "implied_inconsistencies": state.get(
            "implied_inconsistencies", "None identified"
        ),
        "sequential_commitment_issues": state.get(
            "sequential_commitment_issues", "None identified"
        ),
        # Aggregate analyses
        "key_insights": state.get("key_insights", []),
        "critical_issues": state.get("critical_issues", []),
    }

    # Call structured LLM with the fully populated state
    res = call_structured_llm(
        report_state,
        MARKDOWN_REPORT_TEMPLATE,
        MarkdownReport,
        model=LLMConfig.DEFAULT_MODEL,
        temperature=0,
    )

    return {"markdown_report": res.markdown_report}
