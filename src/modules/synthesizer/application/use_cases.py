from .ports import SynthesizerRepository, EmbeddingGenerator, DocumentReader
from ..domain.entities import Axiom, SourceProof, MoltbookIdentity
import hashlib

class IngestDocumentUseCase:
    def __init__(
        self, 
        repository: SynthesizerRepository,
        embedder: EmbeddingGenerator,
        reader: DocumentReader
    ):
        self.repository = repository
        self.embedder = embedder
        self.reader = reader

    def execute(self, file_path: str, author: str, agent_identity: MoltbookIdentity) -> Axiom:
        # 1. Read Content
        content = self.reader.read_file(file_path)
        
        # 2. Generate Hash
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        
        # 3. Generate Embedding
        vector = self.embedder.get_embedding(content)
        
        # 4. Create Source Proof
        source_proof = SourceProof(
            document_name=file_path.split("/")[-1],
            original_author=author,
            content_hash=content_hash,
            page_ref=None # Could be refined if reading by page
        )
        
        # 5. Create Axiom
        axiom = Axiom(
            declaration=content, # The core truth is the content itself for this basic ingestion
            confidence_score=1.0, # Initial ingestion assumed true
            tags=["ingested", "document"],
            source_proof=source_proof,
            moltbook_identity=agent_identity
        )
        
        # 6. Save
        self.repository.save(axiom, vector)
        
        return axiom
