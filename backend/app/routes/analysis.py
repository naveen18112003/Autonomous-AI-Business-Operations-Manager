from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.agents.analysis_agent import analysis_agent
from app.services.data_parser import data_parser
from app.models.agent_models import AnalysisRequest, AnalysisResponse

router = APIRouter()

@router.post("/", response_model=AnalysisResponse)
async def run_analysis(
    file: UploadFile = File(None),
    text_input: str = Form(None)
):
    data_context = ""

    if file:
        content = await file.read()
        if file.filename.endswith('.csv'):
            try:
                data_context += "CSV Data:\n" + data_parser.parse_csv(content) + "\n"
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Invalid CSV file: {str(e)}")
        else:
            data_context += "File content:\n" + content.decode('utf-8') + "\n"

    if not data_context and not text_input:
        raise HTTPException(status_code=400, detail="No data or operational notes provided. Please upload a file or enter notes.")

    request = AnalysisRequest(data=data_context, context=text_input or "")
    result = analysis_agent.run(request)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    return result
