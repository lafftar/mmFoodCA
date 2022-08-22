import asyncio
from asyncio import sleep
from json import dumps
from pprint import pprint
from time import perf_counter

import httpx

from utils.custom_logger import Log

c = None
log: Log = Log('[TESTING API]', do_update_title=False)


def get_c(): return httpx.AsyncClient(timeout=2)


async def test_live_check(host: str):
    global c
    c = get_c()

    path = 'live-check'
    end_str = f' - [{host}] [/{path}]'
    async with c:
        try:
            resp = await c.get(f"{host}/{path}")
            msg = f'{resp.status_code} - {resp.reason_phrase} - {resp.json().get("message")}{end_str}'
            if resp.status_code != 200:
                log.error(msg)
                return msg

            log.info(msg)
            return msg
        except Exception as err:
            err = f'{err}'
            if not err:
                err = f'Exception'

            msg = f'Failed - {err}{end_str}'
            log.error(msg)
            return msg


async def test_all(hosts: list = None):
    t1 = perf_counter()

    if not hosts:
        hosts = [
            f'{protocol}://{host}'
            for host in [
                'localhost:1337',
                '155.138.158.45',
                'mmfood.ca',
                'www.mmfood.ca'
                # '2001:19f0:b001:f77:5400:04ff:fe1c:f19a'
            ]
            for protocol in [
                'http',
                'https'
            ]
            if 'https://localhost' not in f'{protocol}://{host}'  # only want to test http local
        ]

    resp = await asyncio.gather(
        *(
            test_live_check(host) for host in hosts
        )
    )

    result = "\n\t".join(dumps(resp, indent=4).split('\n'))
    msg = '\n' \
          f'\t[{"Test Complete".upper()}]\n' \
          f'\t{result}\n' \
          f'\tTook [{perf_counter() - t1:.2f}]s'
    log.debug(msg)
    return msg


if __name__ == "__main__":
    asyncio.run(test_all())
