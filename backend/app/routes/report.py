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

    import tempfile
    
    filename = f"report_{uuid.uuid4()}.pdf"
    # Use system temp directory (works on Vercel)
    file_path = os.path.join(tempfile.gettempdir(), filename)

    try:
        pdf_service.generate_report(report_content_dict, file_path)
    except Exception as e:
        import traceback
        print(f"PDF ERROR: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=f"PDF Generation failed: {str(e)}")

    return FileResponse(path=file_path, filename=filename, media_type='application/pdf')
