import pytest
from unittest.mock import Mock, ANY
from src.modules.synthesizer.application.use_cases import IngestDocumentUseCase
from src.modules.synthesizer.application.ports import SynthesizerRepository, EmbeddingGenerator, DocumentReader
from src.modules.synthesizer.domain.entities import Axiom, MoltbookIdentity

def test_ingest_document_success():
    # Arrange
    mock_repo = Mock(spec=SynthesizerRepository)
    mock_embedder = Mock(spec=EmbeddingGenerator)
    mock_reader = Mock(spec=DocumentReader)
    
    # Mocks behavior
    mock_reader.read_file.return_value = "This is a test document content."
    mock_embedder.get_embedding.return_value = [0.1, 0.2, 0.3]
    
    use_case = IngestDocumentUseCase(
        repository=mock_repo,
        embedder=mock_embedder,
        reader=mock_reader
    )
    
    identity = MoltbookIdentity(
        agent_id="test-agent",
        karma=10.0,
        cryptographic_signature="sig-123"
    )
    
    # Act
    axiom = use_case.execute(
        file_path="dummy.pdf",
        author="Test Author",
        agent_identity=identity
    )
    
    # Assert
    assert isinstance(axiom, Axiom)
    assert axiom.declaration == "This is a test document content."
    assert axiom.source_proof.original_author == "Test Author"
    assert axiom.source_proof.content_hash is not None
    assert axiom.moltbook_identity == identity
    
    # Verify interactions
    mock_reader.read_file.assert_called_once_with("dummy.pdf")
    mock_embedder.get_embedding.assert_called_once_with("This is a test document content.")
    mock_repo.save.assert_called_once_with(axiom, [0.1, 0.2, 0.3])
