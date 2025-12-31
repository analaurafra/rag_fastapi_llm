from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    prompt: str = Field(..., example="Explique o FastAPI em poucas palavras")

    model_config = {
        "json_schema_extra": {
            "example": {
                "prompt": "Explique o FastAPI em poucas palavras"
            }
        }
    }


class GenerateResponse(BaseModel):
    output: str

