
import os
import chainlit as cl
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from openai.types.responses import ResponseTextDeltaEvent

# Load env
load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Step 1: Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Step 2: Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

# Step 3: Run config
run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

# Step 4: Agent
agent = Agent(
    name="panaversity chatbot",
    instructions="You are a helpful Panaversity chatbot for resolving user questions."
)

# Step 5: Chainlit handler
@cl.on_message
async def on_message(message: cl.Message):
    # 👇 Create an empty message first
    msg = cl.Message(content="")
    await msg.send()

    # Stream into it
    async for event in Runner.run_streamed(agent, input=message.content, run_config=run_config).stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            msg.content += event.data.delta  # append new tokens
            await msg.update()               # update same message
        elif event.type == "response.completed":
            msg.content += "\n✅ Done!"
            await msg.update()
