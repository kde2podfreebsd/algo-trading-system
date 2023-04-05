import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from app.API.handlers import user_router

#########################
# BLOCK WITH API ROUTES #
#########################

# create instance of the app
app = FastAPI(title="crypto-TA trading system")

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8000)
