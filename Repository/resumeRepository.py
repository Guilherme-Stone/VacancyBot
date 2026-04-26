from unittest import result

from sqlalchemy.ext.asyncio import AsyncSession
from Model.resumeModel import ResumeModel
from sqlalchemy import select


class ResumeRepository:

    async def createData(self,db:AsyncSession,resume:str,url:str):
        print(type(resume))
        obj = ResumeModel(resume=resume,url=url)

        db.add(obj)
        await db.commit()

        return


    async def getResume(self,db: AsyncSession):
        results = await db.execute(
            select(ResumeModel.resume)
        )

        objs = results.scalars().all()

        if not objs:
            return []

        return objs

    async def deleteResume(self,url,db:AsyncSession):
       result = await db.execute(
           select(ResumeModel).where(ResumeModel.url == url))

       obj = result.scalars().first()

       if not obj:
           return None

       await db.delete(obj)
       await db.commit()


       return obj

    async def getUrls(self,db:AsyncSession):
        result = await db.execute(
            select(ResumeModel.url)
        )

        obj = result.scalars().all()

        if not obj:
            return []

        return obj



