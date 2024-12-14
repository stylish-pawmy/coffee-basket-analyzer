from pydantic import BaseModel

class RuleDto(BaseModel):
    consequents: list[str]
    antecedents: list[str]
    support: float
    confidence: float
    lift: float