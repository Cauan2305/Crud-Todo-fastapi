from fastapi import FastAPI
from app.routers.v1.users import router as users_router
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from app.core.db.mongo_db import DbErrorOperations
from pydantic import ValidationError
app = FastAPI(
    title="TODO API",
    description="API For TODO Tasks .",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Users",
            "description": "User related endpoints",
        },
        {
            "name": "Tasks",
            "description": "Tasks related endpoints",
        },
    ],
)

@app.exception_handler(ValidationError)
async def validation_error_exception_handler(request: Request, exc: ValidationError):
    """
    Exception handler for ValidationError.

    Args:
        - request (Request): The FastAPI request object.
        - exc (ValidationError): The exception instance.

    Returns:
        - JSONResponse: A JSON response with a 400 status code.
    """
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )



@app.exception_handler(DbErrorOperations)
async def value_error_exception_handler(request: Request, exc: DbErrorOperations):
    """
    Exception handler for DbErrorOperations.

    Args:
        - request (Request): The FastAPI request object.
        - exc (DbErrorOperations): The exception instance.

    Returns:
        - JSONResponse: A JSON response with a 400 status code.
    """
    return JSONResponse(
        status_code=400,
        content={"detail": f"Operation Failure at the database: {str(exc)}"},
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Exception handler for HTTPException.

    Args:
        - request (Request): The FastAPI request object.
        - exc (HTTPException): The exception instance.

    Returns:
        - JSONResponse: A JSON response with the status code and detail message from the exception.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


app.include_router(users_router,prefix="/user",tags=["Users"])

@app.get("/", status_code=status.HTTP_200_OK)
def heartbeat():
    """
    Endpoint for checking the health of the application.

    Returns:
        - dict: A JSON response indicating the application is healthy.
    """
    return {"healthy": True}
