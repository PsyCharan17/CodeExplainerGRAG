from openai import OpenAI
import os
import git
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")

#Use this to install the module 
# pip install -e git+https://github.com/jayavibhavnk/graph-retrieval-system.git#egg=graph-retrieval-system -q
# Or clone the repo and install the required packages and modules 
# git clone https://github.com/jayavibhavnk/graph-retrieval-system.git
# %cd graph-retrieval-system
# !pip install .

from graph_retrieval_system import GraphRAG
grag = GraphRAG()

processed_file_path = 'input.txt' 
def making_graph(file):
  grag.create_graph_from_file(file)

def data_processing(repo_link,input_file_path = processed_file_path):
   merging_files(repo_link)
   making_graph(input_file_path)

def qa_from_graph(query):
  response = grag.queryLLM(query)
  print('answer:',response)
  return response

repo_link = 'https://github.com/PsyCharan17/SampleRepo'
# repo_link = 'https://github.com/PsyCharan17/BlogifyAI'
def merging_files(repo_link):
    project_name = repo_link.split('/')[-1]  # Getting the project name from the URL
    repo_link = repo_link + '.git'

    # Clone the repository
    target_directory = f'tmp/{project_name}'
    if not os.path.exists(target_directory):
      repo = git.Repo.clone_from(repo_link, target_directory, branch='main')
    else:
      print(f"The directory '{target_directory}' already exists. Skipping cloning.")
    
    # Open input.txt file for writing
    with open('input.txt', 'w', encoding='utf-8') as input_file:
        for blob in repo.tree().blobs:  # Traverse through the files in the repository
            # Read the content of each file
            file_content = blob.data_stream.read().decode('utf-8')
            # Write filename and its content into input.txt
            input_file.write("Start of next file \n")
            input_file.write(f"File: {blob.path}\n\n")
            input_file.write(file_content)
            input_file.write("\n\n")

    print('All files merged into input.txt')





if __name__ == '__main__':
  data_processing(repo_link)
  query= "What is happening in the dataprocessor.py file"
  print("Heres the query : ", query)
  qa_from_graph(query)


