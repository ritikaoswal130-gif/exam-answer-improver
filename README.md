\# 📘 Exam Answer Improver (AI-Powered)



An AI-powered web application that evaluates engineering exam answers based on the \*\*actual question\*\*, \*\*subject\*\*, and \*\*marks\*\*, and provides \*\*examiner-style feedback\*\*, \*\*marks allocation\*\*, and an \*\*improved exam-ready answer\*\*.



This project is designed specifically for \*\*Indian engineering students\*\* across multiple branches.



---



\## 🚀 Live Demo

👉 https://exam-answer-improver.onrender.com 



---



\## 🎯 Problem Statement



Engineering students often struggle to:

\- Know \*\*whether their answer is sufficient for the asked marks\*\*

\- Identify \*\*missing points and keywords\*\*

\- Understand \*\*how examiners evaluate answers\*\*

\- Structure answers in an \*\*exam-scoring format\*\*



Traditional practice methods do not provide \*\*instant, examiner-style feedback\*\*.



---



\## 💡 Solution



This application acts like a \*\*virtual university examiner\*\*:



1\. Takes the \*\*exact exam question\*\*

2\. Accepts the \*\*student’s written answer\*\*

3\. Dynamically understands the \*\*engineering branch \& subject\*\*

4\. Internally generates a \*\*model answer\*\*

5\. Evaluates the student’s answer against it

6\. Provides:

&nbsp;  - Marks awarded

&nbsp;  - Coverage analysis

&nbsp;  - Missing concepts

&nbsp;  - Examiner’s comments

&nbsp;  - Improved exam-ready answer



---



\## 🧠 Key Features



\- ✅ Question-based evaluation (not generic correction)

\- ✅ Examiner-style marking logic

\- ✅ Dynamic Branch → Subject selection

\- ✅ Supports multiple engineering branches:

&nbsp; - Information Technology

&nbsp; - Computer Science

&nbsp; - Mechanical Engineering

&nbsp; - Electrical Engineering

&nbsp; - Electronics \& Telecommunication

&nbsp; - Electronics Engineering

\- ✅ Mark-wise answer depth (4, 6, 8, 10 marks)

\- ✅ Clean, student-friendly UI

\- ✅ Deployed live on cloud



---



\## 🛠️ Tech Stack



\*\*Frontend\*\*

\- HTML5

\- CSS3

\- Vanilla JavaScript



\*\*Backend\*\*

\- Python

\- Flask



\*\*AI\*\*

\- OpenAI API (GPT-based evaluation)



\*\*Deployment\*\*

\- Render (Linux server)

\- Gunicorn (production server)



---



\## ⚙️ How It Works (Architecture)



User Question + Answer

↓

Frontend (HTML/CSS/JS)

↓

Flask Backend

↓

AI generates internal model answer

↓

AI compares student answer vs model

↓

Marks + Feedback + Improved Answer



---



\## 📂 Project Structure



exam-answer-improver/

│

├── app.py

├── requirements.txt

├── start.sh

├── README.md

│

├── templates/

│ └── index.html

│

└── static/

└── style.css



---



\## 🧪 Example Use Case



\*\*Question:\*\*  

Explain normalization in DBMS. (6 marks)



\*\*Student Answer:\*\*  

Normalization removes redundancy in databases.



\*\*Output:\*\*  

\- Marks Awarded: 2 / 6  

\- Missing points: Normal forms, functional dependency, example  

\- Examiner comments  

\- Rewritten full-mark exam answer



---



\## 👨‍🎓 Target Users



\- Engineering students (IT, CSE, Mech, Electrical, ENTC, Electronics)

\- Exam preparation and self-evaluation

\- Students aiming to improve \*\*answer quality and structure\*\*



---



\## 🔮 Future Improvements



\- Keyword highlighting

\- Confidence score per answer

\- Subject-wise rubrics

\- User authentication \& history

\- Mobile-friendly UI

\- Bloom’s taxonomy based evaluation



---



\## 📌 Resume Description (Sample)



> Built and deployed an AI-powered exam evaluation platform using Flask and OpenAI that dynamically generates examiner-style feedback by comparing student responses against AI-generated model answers across multiple engineering disciplines.



---



\## 👤 Author



\*\*Ritika Oswal\*\*  

Engineering Student | AI \& Full-Stack Development Enthusiast



---



\## ⭐ Acknowledgements



\- OpenAI API

\- Flask community

\- Render platform



