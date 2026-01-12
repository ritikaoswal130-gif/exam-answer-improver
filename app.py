from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        question = data.get("question", "")
        student_answer = data.get("answer", "")
        subject = data.get("subject", "General")
        marks = data.get("marks", "6")

        subject_guidelines = {
            "Database Management Systems (DBMS)":
            "Focus on definitions, normal forms, redundancy, dependency, and examples.",

            "Operating Systems":
            "Explain working principles, advantages, and OS components.",

            "Computer Networks":
            "Mention layers, protocols, and real-world examples.",

            "Data Structures":
            "Include definitions, operations, and time complexity.",

            "Thermodynamics":
            "Include laws, equations, assumptions, and physical interpretation.",

            "Control Systems":
            "Discuss block diagrams, transfer functions, and stability concepts."
        }

        guideline = subject_guidelines.get(
            subject,
            "Use standard undergraduate engineering exam evaluation style."
        )

        prompt = f"""
You are an Indian engineering university examiner.

You will evaluate a student's answer by first creating an internal model answer
based strictly on the given exam question and marks.

IMPORTANT INSTRUCTIONS:
1. First, internally generate a complete, ideal, exam-scoring model answer
   for the question below, suitable for a {marks}-mark answer.
2. Do NOT display the full model answer in your response.
3. Use the model answer ONLY as a reference to evaluate the student's answer.
4. Compare the student's answer against the model answer to identify:
   - Covered concepts
   - Missing or weak concepts
   - Irrelevant or incorrect points
5. Award marks strictly based on this comparison.

Question:
{question}

Subject-Specific Expectations:
{guideline}

Student Answer:
{student_answer}

STRICT RESPONSE FORMAT:

Marks Awarded: X / {marks}

Coverage Analysis:
- Concepts Covered:
- Concepts Missing:
- Incorrect / Weak Points:

Criteria-wise Evaluation:
- Definition:
- Explanation:
- Keywords:
- Examples / Diagrams:

Examiner’s Comment:
- 1–2 lines of realistic feedback

Improved Exam-Ready Answer:
- Rewrite the answer so it would score full marks
- Follow exam-oriented structure
- Use simple academic language
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            timeout=20
        )

        result = response.choices[0].message.content
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({
            "result": f"⚠️ An error occurred while evaluating the answer:\n{str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

