from fastapi import FastAPI
from .routers.staff_organization import (
    qualifications, staff_departments, staff_roles, archived_qualifications, archived_staff_departments,
    archived_staff_roles
)
from .middleware.error_handler import ExceptionMiddleware
from .logging.logger import logger

version = "v1"
app = FastAPI(
    version = version,
    title = "TraKademik"
)

app.add_middleware(ExceptionMiddleware)


app.include_router(qualifications.router, prefix=f"/api/{version}/staff/qualifications",
                   tags=["Qualifications"])
app.include_router(archived_qualifications.router, prefix=f"/api/{version}/archive/staff/qualifications",
                   tags=["Archived","Qualifications"])


app.include_router(staff_departments.router, prefix=f"/api/{version}/staff/departments",
                   tags=["Staff Departments"])
app.include_router(archived_staff_departments.router, prefix=f"/api/{version}/archive/staff/departments",
                   tags=["Archived", "Staff Departments"])



app.include_router(staff_roles.router, prefix=f"/api/{version}/staff/roles",
                   tags=["Staff Roles"])
app.include_router(archived_staff_roles.router, prefix=f"/api/{version}/archive/staff/roles",
                   tags=["Archived","Staff Roles"])


@app.get("/")
async def root():
    return {"message": "Welcome to TraKademik!"}

logger.info("Application started")