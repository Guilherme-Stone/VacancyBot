from typing import Any
import httpx

from Repository.resumeRepository import ResumeRepository


class JobOutput:

    def __init__(self):
        self.urls = []

    def job_output_data(self,vacancy:list):
         for i in vacancy:
             for j in i:
                k = j['redirect_url']
                self.urls.append(k)

         print("All url's vacancy added to file!")

         if not self.urls:
             return []

         return self.urls

    async def check_url(self, url: str):
        async with httpx.AsyncClient(
                follow_redirects=True,
                timeout=10
        ) as client:
            response = await client.get(url)

        return 200 <= response.status_code < 400







