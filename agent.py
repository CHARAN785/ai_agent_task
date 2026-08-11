from langchain_groq import ChatGroq
from dotenv import load_dotenv
from document_generator import create_word_document

load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)


def generate_agent_response(user_request):
    plan_prompt = f"""
You are an autonomous AI agent.

User request:
{user_request}

Create a simple task plan to complete this request.
Return only numbered steps.
"""

    plan = llm.invoke(plan_prompt).content

    document_prompt = f"""
You are a professional business document writer.

User request:
{user_request}

Task plan:
{plan}

Create a complete professional document.
Include title, introduction, main sections, assumptions if needed, and conclusion.
"""

    document_content = llm.invoke(document_prompt).content

    title_prompt = f"""
Create a short professional document title for this request:
{user_request}

Return only title.
"""

    title = llm.invoke(title_prompt).content.strip()

    file_path = create_word_document(title, document_content)

    return {
        "status": "success",
        "user_request": user_request,
        "agent_plan": plan,
        "document_title": title,
        "document_content": document_content,
        "file_path": file_path
    }