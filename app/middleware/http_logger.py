import random
import string
import logging
import time
from starlette.requests import Request

log = logging.getLogger("uvicorn.errors")

async def log_requests(request: Request, call_next):
    """log_requests.
    :param request:
    :type request: Request
    :param call_next:
    """
    idem = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    log.info(
        f"RID={idem} REGION={request.headers.get('cf-ipcountry')} CLIENT_IP={request.headers.get('cf-connecting-ip')} START REQUEST PATH={request.url.path} METHOD={request.method} "
    )
    start_time = time.time()
    response = await call_next(request)

    process_time = (time.time() - start_time) * 1000
    formatted_process_time = '{0:.2f}'.format(process_time)
    log.info(
        f"RID={idem} COMPLETED={formatted_process_time}ms REQUEST={request.method.upper()} {request.url.path} STATUS_CODE={response.status_code}"
    )

    return response