from simpleeval import simple_eval
from dotenv import load_dotenv
from tavily import TavilyClient
import os
load_dotenv()
def calculator(expression):
    try:
        
        result=simple_eval(expression)
        return result

    except Exception as e:
        return f"An unexpected error occured: {e}"

#print(calculator("18 * 4500"))
#print(calculator("18 % of 4500"))

def search_engine(question):
    try:
        tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
        response = tavily_client.search(question)
        return response["results"][0]["content"]
    
    except Exception as e:
        return f"An unexpected error occured: {e}"

#print(search_engine("Who is Leo Messi?"))


    