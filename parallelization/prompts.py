"""
Legal Document Analysis Prompt Templates

This module contains all prompt templates used in the Legal Document Analyzer workflow.
Templates are organized by category and follow a consistent structure for better maintainability.
"""

from langchain_core.prompts import PromptTemplate

# Document Summary Templates
DOCUMENT_SUMMARY_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Create a comprehensive yet concise summary of the following legal document.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Provide an executive summary of the entire document
    - Identify the key parties and their roles
    - Summarize the main purpose and scope of the document
    - Note key dates, deadlines, and durations
    - Highlight any unusual or particularly important provisions
    
    DOCUMENT TEXT:
    {document_text}
    
    DOCUMENT SUMMARY:
    """
)

# Obligation Analysis Templates
PAYMENT_OBLIGATIONS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract all payment obligations.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all payment amounts, terms, and schedules
    - Note any conditions precedent to payment
    - Identify any penalties or discounts related to payment
    - Note any payment security measures
    - Highlight any financial risks or unusual payment terms
    
    DOCUMENT TEXT:
    {document_text}
    
    PAYMENT OBLIGATIONS SUMMARY:
    """
)

DELIVERY_TIMELINES_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract all delivery timelines.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all delivery dates and milestone deadlines
    - Note any conditions that might affect the timeline
    - Identify any penalties or consequences for delayed delivery
    - Note any extension provisions
    - Highlight any timeline risks or impractical deadlines
    
    DOCUMENT TEXT:
    {document_text}
    
    DELIVERY TIMELINES SUMMARY:
    """
)

REPORTING_REQUIREMENTS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract all reporting requirements.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all required reports and notifications
    - Note frequency and deadlines for each report
    - Identify the required content and format of reports
    - Note any consequences for missed reporting
    - Highlight any unusual or burdensome reporting requirements
    
    DOCUMENT TEXT:
    {document_text}
    
    REPORTING REQUIREMENTS SUMMARY:
    """
)

PERFORMANCE_CRITERIA_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract all performance criteria.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all performance standards and metrics
    - Note any service level agreements (SLAs)
    - Identify any penalties or bonuses tied to performance
    - Note any performance monitoring mechanisms
    - Highlight any unrealistic or vague performance expectations
    
    DOCUMENT TEXT:
    {document_text}
    
    PERFORMANCE CRITERIA SUMMARY:
    """
)

# Risk Analysis Templates
LIABILITY_RISKS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract all liability risks.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all clauses that assign, limit, or exclude liability
    - Note any caps on liability amounts
    - Identify any indemnification clauses
    - Analyze any insurance requirements
    - Highlight particularly concerning liability exposures
    
    DOCUMENT TEXT:
    {document_text}
    
    LIABILITY RISKS SUMMARY:
    """
)

TERMINATION_CONDITIONS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract all termination conditions.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all circumstances under which the agreement can be terminated
    - Note any termination for convenience clauses
    - Identify notice periods required for termination
    - Analyze any consequences or penalties for early termination
    - Note any post-termination obligations
    
    DOCUMENT TEXT:
    {document_text}
    
    TERMINATION CONDITIONS SUMMARY:
    """
)

WARRANTY_GAPS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify any warranty gaps or limitations.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify all warranties provided and their scope
    - Note any warranty disclaimers or limitations
    - Identify standard warranties that might be missing
    - Analyze warranty periods and any conditions
    - Highlight particularly concerning warranty limitations
    
    DOCUMENT TEXT:
    {document_text}
    
    WARRANTY GAPS SUMMARY:
    """
)

FORCE_MAJEURE_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and extract force majeure clauses and their implications.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify any force majeure clauses and their scope
    - Note what events are specifically included or excluded
    - Analyze the consequences of a force majeure event
    - Identify any notification requirements
    - Note any time limitations on force majeure protections
    
    DOCUMENT TEXT:
    {document_text}
    
    FORCE MAJEURE IMPLICATIONS SUMMARY:
    """
)

# Opportunity Analysis Templates
PRICING_LEVERAGE_POINTS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify pricing leverage points.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify favorable pricing terms and conditions
    - Note any price adjustment mechanisms that could be advantageous
    - Identify any volume discounts or incentives
    - Analyze payment term flexibility
    - Note any pricing renegotiation opportunities
    
    DOCUMENT TEXT:
    {document_text}
    
    PRICING LEVERAGE POINTS SUMMARY:
    """
)

CONTRACT_EXTENSION_OPTIONS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify contract extension options.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify any renewal or extension clauses
    - Note the conditions required for extensions
    - Analyze any price adjustments tied to extensions
    - Identify any auto-renewal provisions
    - Note any limitations on the number of extensions
    
    DOCUMENT TEXT:
    {document_text}
    
    CONTRACT EXTENSION OPTIONS SUMMARY:
    """
)

SERVICE_SCOPE_EXPANSION_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify service scope expansion opportunities.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify any clauses that allow for expanded service offerings
    - Note any upsell or cross-sell opportunities defined in the agreement
    - Analyze any mechanisms for adding new services
    - Identify any limitations on scope expansion
    - Note any pricing considerations for expanded services
    
    DOCUMENT TEXT:
    {document_text}
    
    SERVICE SCOPE EXPANSION SUMMARY:
    """
)

EARLY_TERMINATION_ADVANTAGES_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify any early termination advantages.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify any favorable early termination rights
    - Note any circumstances where early termination would be advantageous
    - Analyze penalties or costs associated with early termination
    - Identify notice periods required for termination
    - Note any post-termination benefits or obligations
    
    DOCUMENT TEXT:
    {document_text}
    
    EARLY TERMINATION ADVANTAGES SUMMARY:
    """
)

# Definition Analysis Templates
DEFINED_TERMS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Extract and categorize defined terms from the following legal document.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify terms that are explicitly defined in the document
    - Categorize terms as either industry-specific or contract-specific
    - For each term, provide its precise definition as stated in the document
    - Format as a structured dictionary with term:definition pairs
    - Include ALL defined terms, even if there are many
    
    DOCUMENT TEXT:
    {document_text}
    """
)

DEFINITION_CONSISTENCY_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the consistency of defined terms throughout the legal document.
    
    DOCUMENT TYPE: {document_type}
    
    DEFINED TERMS:
    {terms_text}
    
    REQUIREMENTS:
    - Identify any terms that are used inconsistently throughout the document
    - Note any defined terms that are used with different meanings in different sections
    - Identify any terms that are defined but not used, or used but not defined
    - Note any overlapping or contradictory definitions
    - List each consistency issue as a separate point
    
    DOCUMENT TEXT:
    {document_text}
    
    DEFINITION CONSISTENCY ISSUES:
    """
)

# Cross-Reference Analysis Templates
DIRECT_CONTRADICTIONS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify any direct contradictions.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify statements that directly contradict each other
    - For each contradiction, cite the specific clauses or sections involved
    - Explain the nature of each contradiction
    - Focus on statements that are explicitly in conflict, not just potentially inconsistent
    - List each contradiction as a separate point
    
    DOCUMENT TEXT:
    {document_text}
    
    DIRECT CONTRADICTIONS:
    """
)

IMPLIED_INCONSISTENCIES_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify any implied inconsistencies.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify statements that, while not directly contradictory, create logical inconsistencies
    - For each inconsistency, cite the specific clauses or sections involved
    - Explain the nature of each implied inconsistency
    - Focus on logical conflicts that could create ambiguity in interpretation
    - List each inconsistency as a separate point
    
    DOCUMENT TEXT:
    {document_text}
    
    IMPLIED INCONSISTENCIES:
    """
)

SEQUENTIAL_COMMITMENT_ISSUES_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Analyze the following legal document and identify any sequential commitment issues.
    
    DOCUMENT TYPE: {document_type}
    
    REQUIREMENTS:
    - Identify timeline or sequence conflicts in commitments
    - Note any impossible or challenging sequencing of obligations
    - Identify dependencies that are not properly accounted for
    - Note any deadlines that conflict with each other
    - List each sequential issue as a separate point
    
    DOCUMENT TEXT:
    {document_text}
    
    SEQUENTIAL COMMITMENT ISSUES:
    """
)

# Aggregation Templates
KEY_INSIGHTS_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Based on the analyses below, extract the key insights from this legal document.
    
    DOCUMENT TYPE: {document_type}
    
    ANALYSES:
    {analyses_text}
    
    REQUIREMENTS:
    - Identify up to 10 most important insights from the analyses
    - Focus on high-impact observations that would be valuable to a decision maker
    - Include both risks and opportunities in your insights
    - Be concise and specific for each insight
    - Each insight should be a separate line item
    """
)

CRITICAL_ISSUES_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT ANALYSIS TASK:
    Based on the analyses below, identify critical issues that require immediate attention.
    
    DOCUMENT TYPE: {document_type}
    
    ANALYSES:
    {issues_text}
    
    RISK SCORE: {risk_score}
    
    REQUIREMENTS:
    - Identify 3-5 most critical issues that require immediate attention
    - Focus on issues with high potential impact or legal exposure
    - Each critical issue should be a separate line item
    - For each issue, include a brief explanation of why it's critical
    - Focus only on truly critical issues, not minor concerns
    """
)

MARKDOWN_REPORT_TEMPLATE = PromptTemplate.from_template(
    """
    COMPREHENSIVE LEGAL DOCUMENT ANALYSIS REPORT TASK:
    
    Create a detailed, well-structured markdown report based on the complete analysis of this legal document.
    
    DOCUMENT TYPE: {document_type}
    
    AVAILABLE ANALYSES:
    
    DOCUMENT SUMMARY:
    {document_summary}
    
    RISK SCORE: {risk_score}/100
    OPPORTUNITY SCORE: {opportunity_score}/100
    
    KEY INSIGHTS:
    {key_insights}
    
    CRITICAL ISSUES:
    {critical_issues}
    
    OBLIGATIONS:
    - Payment Obligations: {payment_obligations}
    - Delivery Timelines: {delivery_timelines}
    - Reporting Requirements: {reporting_requirements}
    - Performance Criteria: {performance_criteria}
    
    RISKS:
    - Liability Risks: {liability_risks}
    - Termination Conditions: {termination_conditions}
    - Warranty Gaps: {warranty_gaps}
    - Force Majeure Implications: {force_majeure_implications}
    
    OPPORTUNITIES:
    - Pricing Leverage Points: {pricing_leverage_points}
    - Contract Extension Options: {contract_extension_options}
    - Service Scope Expansion: {service_scope_expansion}
    - Early Termination Advantages: {early_termination_advantages}
    
    DEFINITIONS AND INCONSISTENCIES:
    - Industry-Specific Terms: {industry_specific_terms}
    - Contract-Specific Definitions: {contract_specific_definitions}
    - Definition Consistency Issues: {definition_consistency_issues}
    
    CROSS-REFERENCE ISSUES:
    - Direct Contradictions: {direct_contradictions}
    - Implied Inconsistencies: {implied_inconsistencies}
    - Sequential Commitment Issues: {sequential_commitment_issues}
    
    REQUIREMENTS:
    1. Create a professional, well-structured markdown report with proper headings, sections, and formatting
    2. Include an executive summary at the beginning with overall assessment and key metrics
    3. Organize findings by category (risks, obligations, opportunities, etc.)
    4. Prioritize issues by severity/importance within each section
    5. Include specific references to document sections/clauses where relevant
    6. Add a conclusion with recommendations for next steps
    7. Use markdown formatting effectively (headers, lists, bold for emphasis, tables if appropriate)
    8. Make the report easily scannable for executives
    """
)

# Risk and Opportunity Score Templates
RISK_SCORE_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT RISK ASSESSMENT TASK:
    Based on the analyses below, calculate an overall risk score for this legal document.
    
    DOCUMENT TYPE: {document_type}
    
    ANALYSES:
    1. LIABILITY RISKS:
    {liability_risks}
    
    2. TERMINATION CONDITIONS:
    {termination_conditions}
    
    3. WARRANTY GAPS:
    {warranty_gaps}
    
    4. FORCE MAJEURE IMPLICATIONS:
    {force_majeure_implications}
    
    REQUIREMENTS:
    - Provide a risk score from 0-100, where 0 is minimal risk and 100 is extremely high risk
    - Consider the severity and likelihood of identified risks
    - Provide a brief explanation of the risk assessment
    """
)

OPPORTUNITY_SCORE_TEMPLATE = PromptTemplate.from_template(
    """
    LEGAL DOCUMENT OPPORTUNITY ASSESSMENT TASK:
    Based on the analyses below, calculate an overall opportunity score for this legal document.
    
    DOCUMENT TYPE: {document_type}
    
    ANALYSES:
    1. PRICING LEVERAGE POINTS:
    {pricing_leverage_points}
    
    2. CONTRACT EXTENSION OPTIONS:
    {contract_extension_options}
    
    3. SERVICE SCOPE EXPANSION:
    {service_scope_expansion}
    
    4. EARLY TERMINATION ADVANTAGES:
    {early_termination_advantages}
    
    REQUIREMENTS:
    - Provide an opportunity score from 0-100, where 0 is minimal opportunity and 100 is exceptional opportunity
    - Consider the value and feasibility of identified opportunities
    - Provide a brief explanation of the opportunity assessment
    """
)
