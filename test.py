from agent import run_agent
from agent_retry import run_agent_retry
import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(
  
    api_key=os.environ.get("GROQ_API_KEY"),
)
def judge_answer(question, expected, agent_answer):
    judge_prompt = f"""You are an evaluator grading whether an answer is correct.

    Question: {question}
    Expected answer: {expected}
    Agent's answer: {agent_answer}

    Grading rules:
    - Mark CORRECT if the agent's answer matches the expected meaning, even if worded or formatted differently (e.g. "1/3", "0.333", and "33%" are equivalent).
    - Mark INCORRECT if the answer is wrong, missing, or an error message.
    - Numerical answers that are approximately equal count as correct.

    Reply in exactly this format:
    VERDICT: CORRECT or INCORRECT
    REASON: one short sentence"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": judge_prompt}]
    )
    
    verdict_text = response.choices[0].message.content
    is_correct = "CORRECT" in verdict_text and "INCORRECT" not in verdict_text
    return is_correct, verdict_text



result=[]
correct_count=0
with open("test_set.json", "r") as f:
    test_questions = json.load(f)

#print(test_questions[0]['id'])

#for item in test_questions:
    #print(item['id'])


for item in test_questions:
    question = item["question"]
    expected = item["expected_answer"]

    agent_result = run_agent_retry(question)
    answer_text = agent_result["answer"]            # just the answer text
    tool_used = agent_result["tool_used"]           # the tool (for recording!)
    attempts = agent_result["attempts"]   
    is_correct,verdict=judge_answer(question,expected,answer_text)

    if is_correct:
        correct_count=correct_count+1
    
    result.append({
        "question": question,
        "expected": expected,
        "agent_answer": answer_text,
        "correct": is_correct,
        "judge_verdict": verdict,
        "tool_used": tool_used,             
        "attempts": attempts,               
        "success": agent_result["success"]

    })

    print((f"{'✓' if is_correct else '✗'} {question}"))
    print("Agent_answer: ", answer_text)

score = correct_count / len(test_questions) * 100
print(f"\n Results_modelswap Score: {correct_count}/{len(test_questions)} = {score:.1f}%")

output = {
    "version": "gpt-oss-120b",
    "score_percent": round(score, 1),
    "correct": correct_count,
    "total": len(test_questions),
    "results": result            # ← the whole list nested here
}

with open("results_modelswap.json", "w") as f:
    json.dump(output, f, indent=2)


print("Saved to results_modelswap.json")
