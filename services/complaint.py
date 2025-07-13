from sqlalchemy.ext.asyncio import AsyncSession

from http_client.llm import llm_client
from http_client.sentiment_analysis import SAClient
from constants import llm_prompt
from crud.complaint import create_complaint
from schema.complaint import ComplaintResp
from models.complaints import ComplaintDB
from log.log import logger


async def get_classification_text(session: AsyncSession, text: str) -> ComplaintResp:
    """first classify and then save to db """

    classify_data = await classify_text(text=text)
    saved_data :ComplaintDB= await save_to_db(session=session, body=classify_data)
    return ComplaintResp.model_validate(saved_data.as_dict())


async def classify_text(text: str) -> ComplaintDB:
    """classifying text by category and sentiment using third-party APIs """

    category = await llm_client.llm_process(user_text=text, system_pattern=llm_prompt.text_classification)
    sentiment = await SAClient.find_out_sentiment(text=text)

    result = ComplaintDB(
        text=text,
        category=category,
        sentiment=sentiment
    )
    return result


async def save_to_db(session: AsyncSession, body: ComplaintDB) -> ComplaintDB:
    """ transform body to DB model and save it"""

    try:
        result = await create_complaint(session=session, body=body)
    except Exception as ex:
        logger.error(f"something wrong with save to db! {ex}")
        raise

    logger.info("save to db is successful!")
    return result
