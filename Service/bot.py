from playwright.async_api import async_playwright, Page
import time
from Service.ia_scripts import JobIA
from Repository.resumeRepository import ResumeRepository
from sqlalchemy.ext.asyncio import AsyncSession


from Service.job_output import JobOutput


class JobBot:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self.client = JobIA()

    async def start(self):
            self.playwright = await async_playwright().start()
            self.browser = await self.playwright.chromium.launch(headless=True)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()


    async def close(self):
        if self.page:
            await self.page.close()
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()


    async def send_description(self,urls:list,db:AsyncSession):
        res = ResumeRepository()

        for url in urls:
            await self.page.goto(url)
            text = await self.page.locator("main").inner_text()
            await self.page.get_by_role('link', name="Não, Obrigado(a)").click()
            instruction = """
            Extract information from the vacancy.

            Return ONLY this format:

            City: <city>
            Salary: <salary>
            Requirements: <requirements>

            Do not explain anything.
            Do not write instructions.
            Do not write how to apply.
            """
            resume = await self.client.search_ia(instruction, text)
            await res.createData(resume=resume,url=url,db=db)
            await self.delete_description(url,db)

        return

    async def get_descriptions(self,db:AsyncSession):

        res = ResumeRepository()

        #erro aqui
        data= await res.getResume(db=db)

        if not data:
            return []

        return data

    async def delete_description(self,url:str,db:AsyncSession):
        job_output = JobOutput()
        res = ResumeRepository()
        text = self.page.get_by_text("Candidatar-se").first

        if job_output.check_url == False and text:
            await res.deleteResume(db=db,url=url)
            return True

        return False












