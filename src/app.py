import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.chains import LLMChain


# @cl.on_chat_start
# async def on_chat_start():
#     model = ChatOpenAI(
#         model="gpt-3.5-turbo",
#     )
#
#     prompt = ChatPromptTemplate.from_messages([
#         ("system", "Answer the user's question to the best of your ability."),
#         ("user", "{question}")
#     ])
#     chain = prompt | model | StrOutputParser()
#
#     # Let's save the chain from user_session so we do not have to rebuild
#     # every single time we receive a message
#     cl.user_session.set("chain", chain)
#
#
# @cl.on_message
# async def main(message: cl.Message):
#
#     # Let's load the chain from user_session
#     chain = cl.user_session.get("chain")  # type: LLMChain
#
#     ##########################################################################
#     # Exercise 1d:
#     # Everytime we receive a new user message, we will get the chain from
#     # user_session. We will run the chain with user's question and return LLM
#     # response to the user.
#     ##########################################################################
#     response = await chain.ainvoke(
#         message,
#         callbacks=[cl.LangchainCallbackHandler()]
#     )
#
#     await cl.Message(content=response).send()


model = ChatOpenAI(
        model="gpt-3.5-turbo",
    )

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's question to the best of your ability."),
    ("user", "{question}")
])

chain = prompt | model | StrOutputParser()
print(chain)
