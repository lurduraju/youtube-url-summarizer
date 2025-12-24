# youtube-url-summarizer
# 🔗 LangChain URL & YouTube Video Summarizer

This project is a **Streamlit-based web application** that summarizes content from **YouTube videos** or **web URLs** using **LangChain** and **Groq LLMs**.

It automatically:
- Loads content from a YouTube video or website
- Extracts text (video transcript or webpage text)
- Generates a concise **300-word summary** using an LLM

---

## 🚀 Features

- ✅ Summarize **YouTube videos** using transcripts
- ✅ Summarize **web articles or blogs**
- ✅ Uses **LangChain Summarization Chain**
- ✅ Powered by **Groq LLM (Gemma-7b-it)**
- ✅ Simple and interactive **Streamlit UI**

---

## 🧠 Tech Stack

- **Python**
- **Streamlit** – UI framework
- **LangChain** – Prompt & chain handling
- **Groq LLM** – Fast inference
- **YouTubeLoader** – Transcript extraction
- **UnstructuredURLLoader** – Web content extraction

---

## 📂 Project Structure

```text
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
