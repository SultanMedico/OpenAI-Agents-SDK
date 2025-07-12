# main.py  2. RUN LEVEL  V.V.IMPORTANT  !!!!


from agents import Agent, Runner
from tool import get_config

# Create the agent
agent: Agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
)

# Run the agent synchronously
result = Runner.run_sync(agent,

 "What is Pakistan's full name?"
 
, run_config=get_config())

# Output result
print(result.final_output)
