from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.security import setup_cors
from app.routes import analysis, risk, decision, execution, report

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    root_path="/api"
)

setup_cors(app)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    import traceback
    error_details = traceback.format_exc()
    print("GLOBAL EXCEPTION CAUGHT:\n", error_details)
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal Server Error: {str(exc)}"},
    )

@app.get("/")
def root():
    return {"message": "Autonomous AI Business Ops Manager API is running"}

app.include_router(analysis.router, prefix="/analyze", tags=["analysis"])
app.include_router(risk.router, prefix="/risk", tags=["risk"])
app.include_router(decision.router, prefix="/decision", tags=["decision"])
app.include_router(execution.router, prefix="/execution", tags=["execution"])
app.include_router(report.router, prefix="/report", tags=["report"])
