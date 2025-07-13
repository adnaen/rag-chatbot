from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/ask")
def ask_llm(prompt: str, request: Request):
    context = request.app.state.store.retriever(query=prompt)
    llm_response = request.app.state.llm.ask(query=prompt, context=context)
    return {"assistant": llm_response}
