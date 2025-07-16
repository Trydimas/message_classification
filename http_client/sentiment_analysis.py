import aiohttp
import aiohttp.client_exceptions
import json

from config import settings
from log.log import logger


class SAClient:
    _header = {"apikey": settings.LAYER_API_KEY}
    _url = "https://api.apilayer.com/sentiment/analysis"

    @classmethod
    async def _get_sentiment(cls, text: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=cls._url, data=text, headers=cls._header, timeout=3) as response:
                response.raise_for_status()
                return await response.text()

    @classmethod
    async def find_out_sentiment(cls, text: str) -> str:
        result = None
        try:
            response = await cls._get_sentiment(text)
            result = json.loads(response)
        except Exception as e:
            logger.error(f"Something wrong with sentiment request! {e}")

        return result.get("sentiment")
