from time import perf_counter

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.routing import Mount
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils.root import get_project_root

"""
Get favicon MM logo, and for just logo.
Do About US page first.
"""

routes = [
    Mount(f'/static', StaticFiles(directory=f'{get_project_root()}/server/static'), name='static')
]
templates = Jinja2Templates(directory="templates")
app = FastAPI(routes=routes)


async def home(request: Request):
    """
    Homepage. Hopefully the only other api EP needed.
    @todo - try to figure out pathing in the html and mistypes redirecting to homepage.
    """
    t1 = perf_counter()

    # logic
    pass

    # return
    _ts = f"{perf_counter() - t1:.7f}s"
    headers = {'X-Timer': _ts}
    return templates.TemplateResponse(f"/index.html", {"request": request})


async def live_check() -> JSONResponse:
    """
    'We live baby.'
    """
    t1 = perf_counter()

    # logic
    pass

    # return
    _ts = f"{perf_counter() - t1:.7f}s"
    headers = {'X-Timer': _ts}
    return JSONResponse({'message': 'We live baby.', 'x-timer': _ts}, headers=headers, status_code=200)


# adding routes
app.router.add_api_route(path='/', endpoint=home)
app.router.add_api_route(path='/live-check', endpoint=live_check)


if __name__ == "__main__":
    uvicorn.run('server.api:app', host='localhost', port=1337, reload=True)
