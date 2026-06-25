import os
from dotenv import load_dotenv
from groq import Groq
import json 
from tools import calculator,search_engine
load_dotenv()

tools=[
{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Evaluates a mathematical expression and returns the result. Use this for any arithmetic, percentages, or numerical calculations.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The math expression to evaluate, e.g. '18 * 4500' or '(260-200)/200*100'"
                }
            },
            "required": ["expression"]
        }
    }
},

{
    "type": "function",
    "function": {
        "name": "search_engine",
        "description": "Searches the web for current information, facts, news, or real-world data. Use this for questions about people, places, events, or any information that needs to be looked up.",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The question to search, e.g. 'Who is Leo Messi?'"
                }
            },
            "required": ["question"]
        }
    }
}
]

client = Groq(
  
    api_key=os.environ.get("GROQ_API_KEY"),
)

messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. You have access to a calculator and a web search tool. Use them when needed to answer the user's question accurately."
        },
        {
            "role": "user",
            "content": "What is 18 percent of 4500?",
        }
]

response = client.chat.completions.create(

    model="llama-3.3-70b-versatile",
    tools=tools,
    tool_choice="auto",
    messages=messages,
)
response_message = response.choices[0].message
#print(response_message)
#print(response_message.tool_calls)



available_functions = {
    "calculator": calculator,
    "search_engine": search_engine
}

tool_calls=response_message.tool_calls[0]
function_name = tool_calls.function.name 
function_argument=json.loads(tool_calls.function.arguments)
function_to_call=available_functions[function_name]

result=function_to_call(function_argument["expression"])
#print(f"Result: {result}")

# 1. Append the LLM's tool-request message (so the result has a request to attach to)
messages.append(response_message)

# 2. Append the tool result as a "tool" message
messages.append({
    "role": "tool",
    "tool_call_id": tool_calls.id,
    "content": str(result)
})

# 3. Call the LLM again with the now-fuller conversation
second_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
)

# 4. Print the natural final answer
final_answer = second_response.choices[0].message.content
print("Final answer:", final_answer)