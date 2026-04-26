from Service import job_output
from Service.bot import JobBot
from Service.fetcher import JobFetcher
from Service.job_output import JobOutput
from schema.resumeDto import ResumeDtoResponse, ResumeDtoCreate
from fastapi import HTTPException
import httpx
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import AsyncSession
from playwright.async_api import Error

class ResumeController:

    def __init__(self):
        self.job_bot = JobBot()
        self.job_fetcher = JobFetcher()
        self.job_output = JobOutput()

    async def getParamsFromUser(self,dto:ResumeDtoCreate,db:AsyncSession):
        try:
            urls = []

            data = {
                "where": dto.city,
                "what": dto.position,
                "salary_min": dto.salary_min,
                "salary_max": dto.salary_max,
                "country":dto.country
            }

            vacancy = await self.job_fetcher.search_vacancy(data=data)

            list_vacancy = self.job_output.job_output_data(vacancy)

            for i in list_vacancy:
                urls.append(i)

            if not urls:
                raise HTTPException(status_code=404,detail="The list of urls was empty")

            await self.job_bot.start()
            res = await self.job_bot.send_description(urls=urls,db=db)


            return res

        #error of the API Adzuna or Gemini
        except Exception as e:
            print("ERRO REAL:", type(e), e)
            raise

        except httpx.HTTPStatusError as e:
            print("AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            raise HTTPException(
                status_code=e.response.status_code,
                detail=e.response.text
            )

        #error of connection
        except httpx.RequestError as e:
            raise Exception("ERROR: ",e)

        # database connection
        except OperationalError:
            raise HTTPException(status_code=500, detail="The database did not respond")

        #playwrigth error
        except Error as e:
            raise HTTPException(status_code=500,detail=f"Something went wrong with the bot: {str(e)}")

        finally:
            await self.job_bot.close()



    async def sendResumeToUser(self, db:AsyncSession):
        try:
            res = await self.job_bot.get_descriptions(db=db)

            if not res:
                raise HTTPException(status_code=404, detail="Data not found")

            #ERRO AQUI
            return res

        #database connection
        except OperationalError:
            raise HTTPException(status_code=500,detail="The database did not respond")

        # error of connection
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Connection error: {str(e)}"
            )

        except:
            raise Exception("Url problem...")









