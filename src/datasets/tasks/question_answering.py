from dataclasses import dataclass
from typing import Dict, Optional

from ..features import Features, Value
from .base import TaskTemplate


@dataclass
class QuestionAnswering(TaskTemplate):
    task = "question_answering"
    input_schema = Features({"question": Value("string"), "context": Value("string")})
    label_schema = Features({"answer_start": Value("int32"), "answer_end": Value("int32")})

    def __init__(
        self,
        question_column: str = "question",
        context_column: str = "context",
        answer_start_column: Optional[str] = None,
        answer_end_column: Optional[str] = None,
    ):
        self.question_column = question_column
        self.context_column = context_column
        self.answer_start_column = answer_start_column
        self.answer_end_column = answer_end_column

    @property
    def column_mapping(self) -> Dict[str, str]:
        column_mapping = {
            self.question_column: "question",
            self.context_column: "context",
        }
        if self.answer_start_column and self.answer_end_column:
            column_mapping.update({self.answer_start_column: "answer_start", self.answer_end_column: "answer_end"})
        return column_mapping

    @classmethod
    def from_dict(cls, template_dict: dict) -> "QuestionAnswering":
        return cls(
            question_column=template_dict["question_column"],
            context_column=template_dict["answer_column"],
            answer_start_column=template_dict.get("answer_start_column"),
            answer_end_column=template_dict.get("answer_end_column"),
        )
