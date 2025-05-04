"""
Legal Document Analyzer Workflow

A high-performance, parallel processing pipeline for comprehensive legal document analysis.
This module implements a sophisticated LangGraph workflow that decomposes complex document
analysis into concurrent processing paths to maximize throughput and analytical depth.

Architecture Overview:
1. Document Sectioning - Distributes analysis across 5 specialized parallel paths
2. Sequential Processing - Maintains logical dependencies within each processing track
3. Result Aggregation - Synthesizes distributed analyses into actionable insights

This implementation demonstrates an efficient parallelization pattern for complex
document processing tasks where multiple independent analyses can be conducted simultaneously.
"""

import sys
import os
import argparse
from typing import Annotated, TypedDict, Dict, List

from langgraph.graph import StateGraph, END, START
from parallelization.state import LegalDocumentAnalyzerState

# Import specialized analysis node functions
from parallelization.nodes.summary import generate_document_summary
from parallelization.nodes.obligations import (
    analyze_payment_obligations,
    analyze_delivery_timelines,
    analyze_reporting_requirements,
    analyze_performance_criteria,
)
from parallelization.nodes.risks import (
    analyze_liability_risks,
    analyze_termination_conditions,
    analyze_warranty_gaps,
    analyze_force_majeure_implications,
    calculate_risk_score,
)
from parallelization.nodes.opportunities import (
    analyze_pricing_leverage_points,
    analyze_contract_extension_options,
    analyze_service_scope_expansion,
    analyze_early_termination_advantages,
    calculate_opportunity_score,
)
from parallelization.nodes.definitions import (
    extract_defined_terms,
    analyze_definition_consistency,
)
from parallelization.nodes.cross_reference import (
    identify_direct_contradictions,
    identify_implied_inconsistencies,
    identify_sequential_commitment_issues,
)
from parallelization.nodes.aggregation import (
    aggregate_key_insights,
    identify_critical_issues,
    generate_markdown_report,
)

# Initialize state graph with the typed state container
graph = StateGraph(LegalDocumentAnalyzerState)

# Register all processing nodes to the workflow graph
# Document summarization node (entry point)
graph.add_node("generate_document_summary", generate_document_summary)

# Obligation analysis pipeline nodes
graph.add_node("analyze_payment_obligations", analyze_payment_obligations)
graph.add_node("analyze_delivery_timelines", analyze_delivery_timelines)
graph.add_node("analyze_reporting_requirements", analyze_reporting_requirements)
graph.add_node("analyze_performance_criteria", analyze_performance_criteria)

# Risk assessment pipeline nodes
graph.add_node("analyze_liability_risks", analyze_liability_risks)
graph.add_node("analyze_termination_conditions", analyze_termination_conditions)
graph.add_node("analyze_warranty_gaps", analyze_warranty_gaps)
graph.add_node("analyze_force_majeure_implications", analyze_force_majeure_implications)
graph.add_node("calculate_risk_score", calculate_risk_score)

# Opportunity identification pipeline nodes
graph.add_node("analyze_pricing_leverage_points", analyze_pricing_leverage_points)
graph.add_node("analyze_contract_extension_options", analyze_contract_extension_options)
graph.add_node("analyze_service_scope_expansion", analyze_service_scope_expansion)
graph.add_node(
    "analyze_early_termination_advantages", analyze_early_termination_advantages
)
graph.add_node("calculate_opportunity_score", calculate_opportunity_score)

# Definition analysis pipeline nodes
graph.add_node("extract_defined_terms", extract_defined_terms)
graph.add_node("analyze_definition_consistency", analyze_definition_consistency)

# Cross-reference validation pipeline nodes
graph.add_node("identify_direct_contradictions", identify_direct_contradictions)
graph.add_node("identify_implied_inconsistencies", identify_implied_inconsistencies)
graph.add_node(
    "identify_sequential_commitment_issues", identify_sequential_commitment_issues
)

# Final analysis aggregation and reporting nodes
graph.add_node("aggregate_results", aggregate_key_insights)
graph.add_node("identify_critical_issues", identify_critical_issues)
graph.add_node("generate_markdown_report", generate_markdown_report)

# Define the workflow execution paths

# Initial document processing - Generate comprehensive summary
graph.add_edge(START, "generate_document_summary")

# Branch into 5 parallel analysis pipelines from the document summary

# 1. Obligation Analysis Pipeline - Sequential dependency chain
graph.add_edge("generate_document_summary", "analyze_payment_obligations")
graph.add_edge("analyze_payment_obligations", "analyze_delivery_timelines")
graph.add_edge("analyze_delivery_timelines", "analyze_reporting_requirements")
graph.add_edge("analyze_reporting_requirements", "analyze_performance_criteria")

# 2. Risk Analysis Pipeline - Sequential dependency chain
graph.add_edge("generate_document_summary", "analyze_liability_risks")
graph.add_edge("analyze_liability_risks", "analyze_termination_conditions")
graph.add_edge("analyze_termination_conditions", "analyze_warranty_gaps")
graph.add_edge("analyze_warranty_gaps", "analyze_force_majeure_implications")
graph.add_edge("analyze_force_majeure_implications", "calculate_risk_score")

# 3. Opportunity Analysis Pipeline - Sequential dependency chain
graph.add_edge("generate_document_summary", "analyze_pricing_leverage_points")
graph.add_edge("analyze_pricing_leverage_points", "analyze_contract_extension_options")
graph.add_edge("analyze_contract_extension_options", "analyze_service_scope_expansion")
graph.add_edge(
    "analyze_service_scope_expansion", "analyze_early_termination_advantages"
)
graph.add_edge("analyze_early_termination_advantages", "calculate_opportunity_score")

# 4. Definition Analysis Pipeline - Sequential dependency chain
graph.add_edge("generate_document_summary", "extract_defined_terms")
graph.add_edge("extract_defined_terms", "analyze_definition_consistency")

# 5. Cross-Reference Validation Pipeline - Sequential dependency chain
graph.add_edge("generate_document_summary", "identify_direct_contradictions")
graph.add_edge("identify_direct_contradictions", "identify_implied_inconsistencies")
graph.add_edge(
    "identify_implied_inconsistencies", "identify_sequential_commitment_issues"
)

# Convergence point - Merge all parallel analysis results
graph.add_edge(
    [
        "analyze_performance_criteria",  # Obligations pipeline terminal node
        "calculate_risk_score",  # Risk pipeline terminal node
        "calculate_opportunity_score",  # Opportunities pipeline terminal node
        "analyze_definition_consistency",  # Definitions pipeline terminal node
        "identify_sequential_commitment_issues",  # Cross-reference pipeline terminal node
    ],
    "aggregate_results",
)

# Final report generation sequence
graph.add_edge("aggregate_results", "identify_critical_issues")
graph.add_edge("identify_critical_issues", "generate_markdown_report")
graph.add_edge("generate_markdown_report", END)

# Compile the graph into an executable workflow
workflow = graph.compile()


def analyze_legal_document(document_text: str, document_type: str) -> Dict:
    """
    Execute a comprehensive parallel analysis of a legal document.

    This function serves as the primary entry point for the legal document analysis
    workflow, initializing the state with document content and triggering the
    parallel processing pipelines.

    Args:
        document_text: The complete text content of the legal document to analyze
        document_type: The document classification (e.g., 'Contract', 'Agreement', 'NDA')

    Returns:
        Dict: A comprehensive analysis result containing all extracted insights,
              risk assessments, opportunities, and a structured markdown report
    """
    # Initialize the state with core document information
    initial_state = {
        "document_text": document_text,
        "document_type": document_type,
    }

    # Execute the parallel analysis workflow
    result = workflow.invoke(initial_state)
    return result
