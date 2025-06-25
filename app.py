import gradio as gr
from thefuzz import process, fuzz

# hardcoded dataset of questions and answers
KNOWLEDGE_BASE = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections"
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

SIMILARITY_THRESHOLD = 80 # setting this to 80 for a balance between precision and recall so that the agent can answer a variety of questions without being too weird.

# hardcoding a fallback response for questions outside the dataset
FALLBACK_RESPONSE = "I'm sorry, I can only answer questions related to Thoughtful AI's agents."

# core logic for matching user queries to predefined questions

# extracting the list of predefined questions
def get_predefined_questions():
    return [item["question"] for item in KNOWLEDGE_BASE["questions"]]

# finding the best match for a user query
def find_best_match(user_query: str) -> str | None:
    predefined_questions = get_predefined_questions()
    
    # using fuzzy matching to find the best match using thefuzz library
    best_match = process.extractOne(user_query, predefined_questions, scorer=fuzz.token_set_ratio)
    
    if best_match and best_match[1] >= SIMILARITY_THRESHOLD:
        matched_question = best_match[0]
        for item in KNOWLEDGE_BASE["questions"]:
            if item["question"] == matched_question:
                return item["answer"]
    return None

# function to handle questions
def thoughtful_ai_support_agent(user_message: str, history: list) -> str:
    if not user_message or not user_message.strip():
        return "Fire away a question."

    answer = find_best_match(user_message)
    
    return answer if answer else FALLBACK_RESPONSE

# building UI using Gradio
def build_ui():
    title = "Thoughtful AI - Customer Support Agent"
    description = """
    This is a simple AI agent to help answer your questions about Thoughtful AI's products. Ask me about EVA, CAM, PHIL or anyhting related to our agents.
    """
    
    examples = [
        ["What is EVA?"],
        ["What is CAM"],
        ["What is PHIL?"],
        ["Why use Thoughtful AI's agents?"],
    ]

    # creating an interface 
    chat_interface = gr.ChatInterface(
        fn=thoughtful_ai_support_agent,
        title=title,
        description=description,
        examples=examples,
        theme="soft",
    )
    
    chat_interface.launch(share=False)

if __name__ == "__main__":
    build_ui()