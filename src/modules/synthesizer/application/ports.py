from abc import ABC, abstractmethod
from ..domain.entities import Axiom

class SynthesizerRepository(ABC):
    @abstractmethod
    def save(self, axiom: Axiom, embedding: list[float]) -> None:
        """Persists an Axiom into the vector store with its embedding."""
        pass

class EmbeddingGenerator(ABC):
    @abstractmethod
    def get_embedding(self, text: str) -> list[float]:
        """Generates a vector embedding for the given text."""
        pass

class DocumentReader(ABC):
    @abstractmethod
    def read_file(self, file_path: str) -> str:
        """Reads a file and returns its content as a string."""
        pass

    
    # Future search methods can be added here
    # @abstractmethod
    # def search(self, query: str, limit: int = 10) -> List[Axiom]:
    #     pass
