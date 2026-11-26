from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Chunk:
    text: str
    page: int


@dataclass(frozen=True)
class RagAnswer:
    answer: str
    sources: list[int]


class RagService:
    def __init__(self, retrieve: Callable[[str], list[Chunk]], answer: Callable[[str, list[Chunk]], str]):
        self.retrieve = retrieve
        self.answer_from_context = answer

    def ask(self, question: str) -> RagAnswer:
        chunks = self.retrieve(question)
        if not chunks:
            return RagAnswer("I could not find that information in the document.", [])
        answer = self.answer_from_context(question, chunks)
        return RagAnswer(answer, sorted({chunk.page for chunk in chunks}))


def sample_service() -> RagService:
    chunks = [
        Chunk("Diabetes affects how the body regulates blood glucose.", 1),
        Chunk("Regular activity can improve insulin sensitivity.", 2),
    ]
    return RagService(
        lambda question: chunks,
        lambda question, context: f"According to the document, {context[0].text}",
    )
