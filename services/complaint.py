from sqlalchemy.ext.asyncio import AsyncSession

from http_client.llm import llm_client
from http_client.sentiment_analysis import SAClient
from constants import llm_prompt
from crud.complaint import create_complaint
from schema.complaint import ComplaintModel, ComplaintResp
from log.log import logger


async def get_classification_text(session: AsyncSession, text: str) -> ComplaintResp:
    """first classify and then save to db """

    complaint_data = await classify_text(text=text)
    return await save_to_db(session=session, body=complaint_data)


async def classify_text(text: str) -> ComplaintModel:
    """classifying text by category and sentiment using third-party APIs """

    category = await llm_client.llm_process(user_text=text, system_pattern=llm_prompt.text_classification)
    sentiment = await SAClient.find_out_sentiment(text=text)

    result = ComplaintModel(
        text=text,
        category=category,
        sentiment=sentiment
    )
    return result


async def save_to_db(session: AsyncSession, body: ComplaintModel) -> ComplaintResp:
    """ transform body to DB model and save it"""

    model_data = body.model_dump(exclude_unset=True, exclude_none=True)
    try:
        await create_complaint(session, model_data)
    except Exception as ex:
        logger.error(f"something wrong with save to db! {ex}")
        raise

    logger.info("save to db is successful!")
    return ComplaintResp.model_validate(model_data)
