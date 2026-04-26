import os
from typing import Any
import httpx
from dotenv import load_dotenv



class JobFetcher:

    def __init__(self):
        self.load = load_dotenv()

    async def search_vacancy(self,data:dict[str,Any]):

        #it's necessary because we need to open and close de requisition
        async with httpx.AsyncClient(timeout=30.0) as client:
            page_list = []

            for pages in range(1,6):
                endpoint = f"https://api.adzuna.com/v1/api/jobs/{data.get("country")}/search/{pages}"
                print("country:", repr(data.get('country')))
                print("endpoint:", endpoint)
                params = {
                    'app_id':os.getenv('ADZUNA_APP_ID'),
                    'app_key':os.getenv('ADZUNA_APP_KEY'),
                    'where': data.get("where"),
                    'what':data.get("what"),
                    'results_per_page':50,
                    'salary_min':data.get("salary_min"),
                    'salary_max':data.get("salary_max"),
                }

                req = await client.get(endpoint, params=params)
                req.raise_for_status()

                response_data = req.json()
                page_list.append(response_data["results"])
        return page_list

