# src/schema.py
from pydantic import BaseModel, Field
from typing import List, Optional

class PropertyBoundaries(BaseModel):
    east: Optional[str] = Field(default=None, description="East boundary details or blank")
    west: Optional[str] = Field(default=None, description="West boundary details or blank")
    north: Optional[str] = Field(default=None, description="North boundary details or blank")
    south: Optional[str] = Field(default=None, description="South boundary details or blank")

class TitleChainStep(BaseModel):
    step_number: int = Field(description="Step sequence number in ownership history")
    owner_name: str = Field(description="Name of the property owner in this step")
    transfer_type: str = Field(description="Type of transfer e.g. Khasra Record, Co-Ownership Deed, Sale Deed")
    deed_details: Optional[str] = Field(default=None, description="Deed number, registration date, or record year")
    share_percentage: Optional[str] = Field(default=None, description="Ownership share e.g. 100%, 50%")

class LegalReportExtractionSchema(BaseModel):
    sub_registrar_office: Optional[str] = Field(default=None, description="Extracted office or None if blank")
    district: Optional[str] = Field(default=None, description="District name or None if blank")
    loan_account_no: Optional[str] = Field(default=None, description="Loan Account Number or None if blank")
    
    flat_no: Optional[str] = Field(default=None)
    plot_no_and_address: Optional[str] = Field(default=None)
    total_area_sq_m: Optional[str] = Field(default=None)
    boundaries: PropertyBoundaries
    
    present_owners: Optional[str] = Field(default=None, description="Current owner name mentioned")
    ownership_flow_chain: List[TitleChainStep] = Field(
        description="Sequential step-by-step history of property transfers"
    )