from email import header
from tempfile import template
import dot_env
from dotenv import load_env
import validators,streamlit as st

from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader


#streamlit app
st.set_page_config(page_title="Langchain:summarize from YT Url or website",page_icon="")
st.title("Summarize text from YT video or Url")
st.subheader("summarize UrL")
with st.sidebar:
    groq_api_key=st.text_input("Groq api key",type="password")
url=st.text_input("URL",label_visibility="collapsed")

llm=ChatGroq(model="Gemma-7b-It",groq_api_key=groq_api_key)

prompt_temp="""
provide the summary of the content in 300 words:
{text}
"""

prompt=PromptTemplate(template=prompt_temp,input_variables=["text"])

if st.button("summarize the url"):
    ## validate all inputs
    if not groq_api_key or not url.strip():
        st.error("please provide the imformation")
    elif not validators.url(url):
        st.error("Please provide the valid url")
    else:
        try:
            with st.spinner("waiting.."):
                if "youtube.com" in url:
                    loader=YoutubeLoader.from_youtube_url(url,add_video_info=true)
                else:
                    loader=UnstructuredURLLoader(urls=[url],ssl_verify=false,
                                                 headers={})
            docs=loader.load()
            chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
            out_summary=chain.run(docs)
            st.sucess(out_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")

"""
🎬 How transcript generation works (full flow)
1. Load the model
from openai import OpenAI
client = OpenAI()

2. Give audio
audio_file = open("audio.mp3", "rb")

3. Ask Whisper to transcribe
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

4. Get text
print(transcript.text)
"""