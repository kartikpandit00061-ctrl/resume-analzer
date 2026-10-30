import streamlit as st
import matplotlib .pyplot as plt
from sklearn .feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk .tokenize import word_tokenize
from nltk import pos_tag


# Dowload NLTK resources

# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("averaged_perceptron_tragger_eng")


           # page setup

st. set_page_config()
st.title("Resume Analyzer")
st.write("Application is working!")
st.header("Upload your Resume")
uploaded_file = st.file_uploader("Upload your resume(PDF)",type=["pdf"])
job_description = st.text_area("paste job Description Here")
if uploaded_file is not None:st.success("Resume uploaded successfully!")
if job_description:st.write("job descrpton added.")