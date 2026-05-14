from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import search_account_balance, send_email, transfer_funds
from langchain.tools import tool
from prompts import SYSTEM_PROMPT
load_dotenv()
#llm
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature =0.1)
#Tools
tools = [send_email, transfer_funds, search_account_balance]

#scratchpad
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])
#Create agent
agent = create_tool_calling_agent(model, tools,prompt)
#Excutuing agent
excution = AgentExecutor(agent=agent, tools=tools,verbose=True)



