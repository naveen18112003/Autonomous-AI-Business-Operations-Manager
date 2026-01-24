from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.agents.reporting_agent import reporting_agent
from app.services.pdf_service import pdf_service
from app.models.agent_models import ReportRequest
import os
import uuid

router = APIRouter()

@router.post("/")
async def generate_report(request: ReportRequest):
    report_content_dict = reporting_agent.run(request)

    if "error" in report_content_dict:
        raise HTTPException(status_code=500, detail=report_content_dict["error"])

    filename = f"report_{uuid.uuid4()}.pdf"
    file_path = f"temp_{filename}" # Ideally into a proper temp dir

    try:
        pdf_service.generate_report(report_content_dict, file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF Generation failed: {str(e)}")

    return FileResponse(path=file_path, filename=filename, media_type='application/pdf')
