from fastapi import APIRouter, Depends
from Controller.controleResume import ResumeController
from sqlalchemy.ext.asyncio import AsyncSession
from Config.settings import get_db
from schema.resumeDto import ResumeDtoCreate, ResumeDtoResponse

router = APIRouter()

@router.post("/vacancy-send-params")
async def getParams(dto:ResumeDtoCreate,db: AsyncSession = Depends(get_db)):
    cr = ResumeController()
    await cr.getParamsFromUser(dto,db)
    return {"message":"resumes successfully created!"}

#the response_model it's who will send to user the data that is expected
@router.get("/vancacy-resumes",response_model=list[str])
async def getResume(db: AsyncSession = Depends(get_db)):
    cr = ResumeController()
    result = await cr.sendResumeToUser(db)
    return result