from fastapi import FastAPI
from fastapi import HTTPException, Body, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import logging

from schemas import GenerateRequest, GenerateResponse
from ai_service import generate_text
from rag.retriever import retrieve_context

app = FastAPI()

logger = logging.getLogger("uvicorn.error")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Try to read JSON body (best-effort) for debugging
    body = None
    try:
        body = await request.json()
    except Exception:
        try:
            raw = await request.body()
            body = raw.decode("utf-8", errors="ignore")
        except Exception:
            body = None

    logger.error("Request validation error: %s; body=%s", exc.errors(), body)
    return JSONResponse(status_code=422, content={"detail": exc.errors(), "body": body})

@app.get("/")
def root():
    return {"status": "ok", "endpoints": ["/ai/generate", "/health"]}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ai/generate", response_model=GenerateResponse)
def generate(
    req: GenerateRequest = Body(
        ...,
        example={"prompt": "Explique o FastAPI em poucas palavras"},
    )
):
    try:
        context = retrieve_context(req.prompt)
        # pass prompt + retrieved context to generator
        output = generate_text(f"{req.prompt}\n\nContext:\n{context}")
        return GenerateResponse(output=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
