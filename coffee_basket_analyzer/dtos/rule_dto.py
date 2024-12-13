from pydantic import BaseModel

class RuleDto(BaseModel):
    consequent: list[str]
    antiscident: list[str]
    support: float
    confidence: float
    lift: float