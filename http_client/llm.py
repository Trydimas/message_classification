from openai import AsyncAzureOpenAI
import copy
from log.log import logger
from config import settings
import tiktoken


class LLMClient:

    def __init__(self, api_version, endpoint, api_key, model, version_model):
        self.client = AsyncAzureOpenAI(
            api_version=api_version,
            azure_endpoint=endpoint,
            api_key=api_key
        )
        self.model = model
        self.encoding = tiktoken.encoding_for_model(version_model)

    async def _send_prompt(self, prompt: list[dict]) -> str:
        """sends a request to self.model"""

        completion = await self.client.chat.completions.create(
            model=self.model,
            messages=prompt,  # type: ignore
            temperature=0
        )
        return completion.choices[0].message.content

    def _assemble_prompt(self, user_text: str, system_pattern: list[dict]) -> list[dict]:
        """assemble prompt from system prompt and user text"""

        prompt = copy.deepcopy(system_pattern)

        for chunk in self._split_text(text=user_text):
            prompt.append(
                {
                    "role": "user",
                    "content": chunk
                }
            )

        return prompt

    def _split_text(self, text: str, overlap=25, chunk_size=150) -> list[str]:
        """if the text is large, then it divides it."""

        text_token = self.encoding.encode(text)
        num_tokens = len(text_token)

        if num_tokens <= chunk_size:
            return [text]

        step = int(chunk_size - overlap)
        chunks = []
        for i in range(0, num_tokens, step):
            chunk = text_token[i:(i + chunk_size)]
            chunks.append(
                self.encoding.decode(chunk)
            )
        return chunks

    async def llm_process(self, user_text: str, system_pattern: list[dict]) -> str | None:
        """handles any task depending on system_pattern"""

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
    model=settings.AZURE_DEPLOYMENT_NAME,
    api_key=settings.AZURE_API_KEY,
    version_model=settings.AZURE_MODEL_NAME
)
