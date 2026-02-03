import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

from src.modules.synthesizer.infrastructure.repository import QdrantSynthesizerRepository
from src.modules.synthesizer.infrastructure.processing import EmbeddingService, DocumentProcessor
from src.modules.synthesizer.application.use_cases import IngestDocumentUseCase
from src.modules.synthesizer.domain.entities import MoltbookIdentity
from config.settings import settings

def main():
    print("=== Axiomind Ingestion Demo ===")
    print(f"Target Qdrant: {settings.QDRANT_HOST}:{settings.QDRANT_PORT}")
    
    try:
        repo = QdrantSynthesizerRepository()
        print("✅ Connected to Qdrant and ensured 'axioms' collection.")
    except Exception as e:
        print(f"❌ Failed to connect to Qdrant: {e}")
        print("👉 Ensure Docker is running: `docker-compose up -d qdrant`")
        return

    print("Initializing Embedding Service (Ollama)...")
    try:
        # Assuming 'nomic-embed-text' is available. 
        # User might need to run `ollama pull nomic-embed-text`
        embedder = EmbeddingService(model_name="nomic-embed-text")
        print("✅ Embedding Service ready.")
    except Exception as e:
        print(f"❌ Failed to init Embeddings: {e}")
        return

    reader = DocumentProcessor()
    use_case = IngestDocumentUseCase(repo, embedder, reader)
    
    identity = MoltbookIdentity(
        agent_id="CLI-Manual",
        karma=100.0,
        cryptographic_signature="sig-demo"
    )
    
    file_path = "data/dummy.txt"
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    print(f"🚀 Ingesting {file_path}...")
    try:
        axiom = use_case.execute(file_path, "Admin User", identity)
        print("\n🎉 Success! Axiom Created:")
        print(f"   ID: {axiom.id}")
        print(f"   Truth: {axiom.declaration[:50]}...")
        print(f"   Hash: {axiom.source_proof.content_hash}")
        print(f"   Karma: {axiom.moltbook_identity.karma}")
        print("\n Check Qdrant Dashboard to see the vector.")
    except Exception as e:
        print(f"❌ Error during ingestion: {e}")

if __name__ == "__main__":
    main()
