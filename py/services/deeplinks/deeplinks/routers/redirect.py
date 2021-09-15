import uuid

from fastapi import APIRouter, HTTPException, Request
from starlette.responses import RedirectResponse

from deeplinks.use_cases.redirect import hit_use_case

router = APIRouter()


@router.get("/d/{id}", tags=["redirect"])
async def redirect(id: str, request: Request):
    client_id = request.cookies.get("_cid") or uuid.uuid4().hex

    url = await hit_use_case(
        id=id,
        client_id=client_id,
        client_user_ip=request.client.host,
        client_user_agent=request.headers.get("User-Agent"),
        document_referer=request.headers.get("Referer"),
    )

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    response = RedirectResponse(url=url, status_code=301)
    response.set_cookie(key="_cid", value=client_id)
    return response
