from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import SimpleDirectoryReader
from ..application.ports import EmbeddingGenerator, DocumentReader
import os

class EmbeddingService(EmbeddingGenerator):
    def __init__(self, model_name: str = "nomic-embed-text", base_url: str = "http://localhost:11434"):
        self.model = OllamaEmbedding(
            model_name=model_name,
            base_url=base_url,
            ollama_additional_kwargs={"mirostat": 0}
        )

    def get_embedding(self, text: str) -> list[float]:
        return self.model.get_text_embedding(text)

class DocumentProcessor(DocumentReader):
    def read_file(self, file_path: str) -> str:
        """Reads a file and returns combined text content."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
            
        reader = SimpleDirectoryReader(input_files=[file_path])
        documents = reader.load_data()
        # Combine all parts into one text for the Axiom (simplification)
        full_text = "\n\n".join([doc.text for doc in documents])
        return full_text
