from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage

messages = [
    SystemMessage(content="You are a helpful assistant that can answer questions about the size of cities."),
]

llm_with_tools = llm.bind_tools(tools=[get_current_datetime])

### 綁定工具之後，大模型沒有直接回答問題， content字為空。大模型發出了工具請求 additional_kwargs 中 有 tool_calls
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model=llm, tools=[get_current_datetime])

messages = agent.invoke(input=dict(message=messages))

response.keys()

for msg in response[messages]:
    msg.pretty_print()