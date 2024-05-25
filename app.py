import streamlit as st
import requests
import tempfile
import os
import importlib.util
from first import data_processing, qa_from_graph

# UI for entering the GitHub repository URL
st.title('GitHub Repository Question Answering App')
repo_url = st.text_input('Enter the GitHub Repository URL:')
if st.button('Process Github Repository'):
  if repo_url:
      st.write("GitHub URL is taken in")
      result = data_processing(repo_url)
      st.success(result)
      query = st.text_input('Enter your query')
      if query:  # Check if a query is provided
          qa_result = qa_from_graph(query)  # Pass the query parameter
          st.text( qa_result)
      else:
        st.warning("Please enter a query.")
  else:
      st.error("Please enter a valid URL.")

