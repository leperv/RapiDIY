# RapiDIY
After seeing an internal tool developed by Matan Yungman, I spun up my own basic version, called RapiDIY (Rapid Do It Yourself).

## What is RapiDIY?
RapiDIY is a very barebones attempt at a general SQL optimization engine.
RapiDIY uses prompts for an AI chatbot, such as Claude or ChatGPT, but my version will prompt a local model that runs with ollama. 

  ### How does RapiDIY work?
  In the project I was shown, the tool had 3 parts:
  - The UI - self-explanatory
  - The Engine - the engine takes the query from the UI, then prompts the LLM, receives the output, and then compares the runtimes between the original query and the modified one to see if the LLM output is better.
  - The "Recipes" - there are some general things that can cause performance issues. A "recipe" is a prompt that handles such a case, for example, not having an ON clause in a JOIN statement that creates a Cartesian join and hampers performance.


### major credit to Matan Yungman for inspiring this little project
