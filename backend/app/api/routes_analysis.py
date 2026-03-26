from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/analyze")
async def analyze_pgn(file: UploadFile = File(...)):
    content = await file.read()

    return {
        "filename": file.filename,
        "size_bytes": len(content),
        "message": "PGN received successfully"
    }