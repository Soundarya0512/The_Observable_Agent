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