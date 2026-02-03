from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class SourceProof(BaseModel):
    document_name: str
    original_author: str
    content_hash: str  # Huella digital
    page_ref: Optional[int] = None

class MoltbookIdentity(BaseModel):
    agent_id: str
    karma: float
    cryptographic_signature: str

class Axiom(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    declaration: str  # Core Truth
    confidence_score: float
    tags: List[str] = Field(default_factory=list)
    source_proof: SourceProof
    moltbook_identity: MoltbookIdentity
    created_at: datetime = Field(default_factory=datetime.utcnow)
