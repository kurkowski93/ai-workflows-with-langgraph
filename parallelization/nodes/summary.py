"""
Document Summary Generator

This module provides the initial document processing functionality that generates
a comprehensive summary of the legal document. This summary serves as the foundation
for all subsequent specialized analyses.
"""

from parallelization.state import LegalDocumentAnalyzerState
from parallelization.prompts import DOCUMENT_SUMMARY_TEMPLATE
from parallelization.utils import call_llm_with_template, create_analysis_function


# Generate document summary using the analysis function factory
generate_document_summary = create_analysis_function(
    DOCUMENT_SUMMARY_TEMPLATE, "document_summary"
)

# Można też użyć bezpośredniego podejścia:
# def generate_document_summary(state: LegalDocumentAnalyzerState):
#     """Generate a summary of the legal document."""
#     result = call_llm_with_template(state, DOCUMENT_SUMMARY_TEMPLATE)
#     return {"document_summary": result}
