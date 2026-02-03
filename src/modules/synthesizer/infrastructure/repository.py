from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from ...application.ports import SynthesizerRepository
from ...domain.entities import Axiom
from config.settings import settings

class QdrantSynthesizerRepository(SynthesizerRepository):
    COLLECTION_NAME = "axioms"
    # Default dimension for many local models (e.g., nomic-embed-text). 
    # Ideally this should match the actual embedding model used.
    VECTOR_SIZE = 768 

    def __init__(self):
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )
        self._ensure_collection()

    def _ensure_collection(self):
        if not self.client.collection_exists(self.COLLECTION_NAME):
            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=self.VECTOR_SIZE,
                    distance=Distance.COSINE
                )
            )

    def save(self, axiom: Axiom, embedding: list[float]) -> None:
        payload = axiom.model_dump(mode='json', exclude={'id'})
        
        point = PointStruct(
            id=axiom.id,
            vector=embedding,
            payload=payload
        )
        
        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=[point]
        )
