from typing import List, Optional, Dict, TypedDict, Any


class LegalDocumentAnalyzerState(TypedDict, total=False):
    """
    State container for the Legal Document Analyzer workflow.

    This TypedDict defines the complete state schema for the parallelized document
    analysis workflow, storing both input parameters and the outputs from each
    processing node in the system.
    """

    # Document inputs
    document_text: str  # Complete text content of the legal document
    document_type: str  # Document classification (contract, agreement, NDA, etc.)

    # Document summary
    document_summary: Optional[str]  # Executive summary with key document highlights

    # Financial and Operational Obligations
    payment_obligations: Optional[
        str
    ]  # Financial terms, amounts, and payment schedules
    delivery_timelines: Optional[str]  # Delivery deadlines and milestone commitments
    reporting_requirements: Optional[
        str
    ]  # Required reports, cadence, and submission criteria
    performance_criteria: Optional[
        str
    ]  # Service levels, metrics, and performance standards

    # Risk Assessment
    liability_risks: Optional[str]  # Liability provisions, limitations, and exposures
    termination_conditions: Optional[
        str
    ]  # Contract termination triggers and procedures
    warranty_gaps: Optional[str]  # Warranty limitations, exclusions, and protections
    force_majeure_implications: Optional[
        str
    ]  # Force majeure provisions and impact analysis

    # Strategic Opportunities
    pricing_leverage_points: Optional[str]  # Advantageous pricing terms and conditions
    contract_extension_options: Optional[
        str
    ]  # Renewal mechanisms and extension provisions
    service_scope_expansion: Optional[
        str
    ]  # Opportunities for expanded service offerings
    early_termination_advantages: Optional[
        str
    ]  # Favorable early termination conditions

    # Terminology Analysis
    industry_specific_terms: Optional[str]  # Industry terminology and definitions
    contract_specific_definitions: Optional[str]  # Contract-specific term definitions
    definition_consistency_issues: Optional[
        str
    ]  # Inconsistencies in term usage and definition

    # Consistency Validation
    direct_contradictions: Optional[str]  # Explicitly contradictory clauses
    implied_inconsistencies: Optional[
        str
    ]  # Logically inconsistent provisions across sections
    sequential_commitment_issues: Optional[
        str
    ]  # Timeline conflicts and sequential dependencies

    # Analysis Results and Metrics
    key_insights: Optional[
        List[str]
    ]  # Principal findings across all analysis dimensions
    risk_score: Optional[float]  # Quantified risk assessment (0-100 scale)
    opportunity_score: Optional[
        float
    ]  # Quantified opportunity assessment (0-100 scale)
    critical_issues: Optional[List[str]]  # High-priority concerns requiring attention
    markdown_report: Optional[str]  # Comprehensive analysis report in markdown format
