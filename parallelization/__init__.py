"""
Legal Document Analysis with Parallel Processing

This package implements a high-performance document analysis system using a parallelized
workflow architecture. It enables comprehensive legal document review by decomposing
analysis tasks into concurrent processing tracks that execute simultaneously.
"""

from parallelization.graph import analyze_legal_document

__all__ = ["analyze_legal_document"]
