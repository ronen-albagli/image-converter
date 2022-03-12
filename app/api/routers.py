from app.api.convert import convertor_router


def init_routers(app):
    app.include_router(convertor_router)
