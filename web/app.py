from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import json
import os

app = FastAPI(title="HR Analytics Dashboard")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    quality_data = {}
    if os.path.exists('/reports/quality_report.json'):
        with open('/reports/quality_report.json', 'r', encoding='utf-8') as f:
            quality_data = json.load(f)

    research_data = {}
    if os.path.exists('/reports/research_summary.json'):
        with open('/reports/research_summary.json', 'r', encoding='utf-8') as f:
            research_data = json.load(f)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "quality": quality_data,
        "research": research_data
    })

@app.get("/plots/{filename}")
async def serve_plot(filename: str):
    plot_path = f"/plots/{filename}"
    if os.path.exists(plot_path):
        return FileResponse(plot_path)
    return {"error": "Графік не знайдено"}

@app.get("/metrics")
def get_metrics():
    return Response(content="hr_app_status 1\n", media_type="text/plain")
