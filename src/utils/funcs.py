"""custom python functions"""



import logging



log = logging.getLogger(__name__)



async def coro_blank():
    """blank coroutine (prints 'no coro given')"""
    pass



async def threadsafe_handled(coro=None):
    """for `asyncio.run_coroutine_threadsafe` only!!
    ---
    \n
    -----------------------------------
    \n
    runs coro with Exception logging
    """
    if coro!=None:
        try:
            await coro
        except Exception as err:
            log.error(err, exc_info=True)
    else:
        await coro_blank()
        log.warning("no coro given!")