"""
Obligation Analysis Pipeline

This module implements the obligation analysis track of the legal document analyzer.
It extracts and analyzes financial and operational commitments including payment terms,
delivery requirements, reporting obligations, and performance standards.
"""

from parallelization.state import LegalDocumentAnalyzerState
from parallelization.prompts import (
    PAYMENT_OBLIGATIONS_TEMPLATE,
    DELIVERY_TIMELINES_TEMPLATE,
    REPORTING_REQUIREMENTS_TEMPLATE,
    PERFORMANCE_CRITERIA_TEMPLATE,
)
from parallelization.utils import create_analysis_function


# Payment analysis processor
analyze_payment_obligations = create_analysis_function(
    PAYMENT_OBLIGATIONS_TEMPLATE, "payment_obligations"
)

# Delivery timeline analysis processor
analyze_delivery_timelines = create_analysis_function(
    DELIVERY_TIMELINES_TEMPLATE, "delivery_timelines"
)

# Reporting requirements analysis processor
analyze_reporting_requirements = create_analysis_function(
    REPORTING_REQUIREMENTS_TEMPLATE, "reporting_requirements"
)

# Performance criteria analysis processor
analyze_performance_criteria = create_analysis_function(
    PERFORMANCE_CRITERIA_TEMPLATE, "performance_criteria"
)
