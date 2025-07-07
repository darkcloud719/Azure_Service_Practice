from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage
import datetime

from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model=llm, tools=[get_current_datetime, get_quanta_computer_price])

def get_current_datetime():

    now = datetime 

def get_quanta_computer_price(model:str="A") -> float:
    # 很重要給LLM看
    """
        Get the price of a Quanta computer model.
        Args:
            model (str): The model of the Quanta computer. Default is "A"
        Returns:
            str: The price of the Quanta computer model
    """
    
    if not isinstance(model, str) or model not in ("A","B","C"):
        raise ValueError("Model must be one of 'A', 'B', or 'C'")
    if model == "A":
        return 1.5
    if model == "B":
        return 1.3
    else:
        return 1.0
    
