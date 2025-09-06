from models.llm import open_ai_llm
from exception.exceptions import format_exception
import json
from langchain_core.messages import HumanMessage
from prompt_library.request_sys_msg import request_system_message

def request_llm(human_message) -> dict:
    try:
        human_msg = HumanMessage(content=human_message)
        response = open_ai_llm.invoke([request_system_message, human_msg])
        response_json = json.loads(response.content)
        return response_json
    except Exception as e:
        error_details = format_exception(e)
        return error_details