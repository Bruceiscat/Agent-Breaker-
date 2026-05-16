from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_anthropic import ChatAnthropic
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from tools import search_account_balance, send_email, transfer_funds
from prompts import SYSTEM_PROMPT

load_dotenv()

model = ChatAnthropic(model="claude-haiku-4-5", temperature=0.1)

tools = [send_email, transfer_funds, search_account_balance]

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

agent = create_tool_calling_agent(model, tools, prompt)
excution = AgentExecutor(agent=agent, tools=tools, verbose=True)
