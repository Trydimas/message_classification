from openai import AsyncAzureOpenAI
import copy
from log.log import logger
from config import settings


class LLMClient:

    # TODO add optimization by tokens and etc

    def __init__(self, api_version, endpoint, api_key, model):
        self.client = AsyncAzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=api_key
        )
        self.model = model

    async def _send_prompt(self, prompt: list[dict]):
        completion = await self.client.chat.completions.create(
            model=self.model,
            messages=prompt,  # type: ignore
        )
        return completion.choices[0].message.content

    def _assemble_prompt(self, user_text: str, system_pattern: list[dict]) -> list[dict]:
        prompt = copy.deepcopy(system_pattern)
        prompt.append(
            {
                "role": "user",
                "content": user_text
            }
        )

        return prompt

    async def llm_process(self, user_text: str, system_pattern: list[dict]):
        prompt = self._assemble_prompt(user_text=user_text, system_pattern=system_pattern)
        result = None
        try:
            result = await self._send_prompt(prompt)
        except Exception as ex:
            logger.error(f"Something wrong with llm request! {ex}")

        logger.info("request to the llm was successful")
        return result


llm_client = LLMClient(
    api_version=settings.AZURE_API_VERSION,
    endpoint=settings.AZURE_ENDPOINT,
    model=settings.AZURE_MODEL,
    api_key=settings.AZURE_API_KEY

)

