from spaceship.app import make_app
from spaceship.config import Settings

app = make_app(Settings())

@app.on_event("startup")
async def startup_event():
   print("Application is starting up...")