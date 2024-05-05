from fastapi import FastAPI
import routes.controller as controller


app = FastAPI()

app.include_router(controller.controller)

