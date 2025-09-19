import asyncio
import os
from dotenv import load_dotenv, find_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

agent = Agent(
    name="Panaversity Chatbot",
    instructions="You are a helpful assistant."
)

async def main():
    result = Runner.run_streamed(
        agent,                     # ✅ just pass agent positional
        "Stream a one-liner.",     # ✅ input positional
        run_config                 # ✅ config positional
    )

    async for event in result.stream_events():
        if event.type == "response.delta":
            print(event.delta, end="", flush=True)
        elif event.type == "response.completed":
            print("\n✅ Done!")

if __name__ == "__main__":
    asyncio.run(main())
