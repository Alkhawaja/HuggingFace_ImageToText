import streamlit as st
import os
import requests
import pandas as pd

st.title("ImageToText with HuggingFace 🤗")

models=["microsoft/git-base","microsoft/trocr-large-printed","Salesforce/blip-image-captioning-large","nlpconnect/vit-gpt2-image-captioning","facebook/nougat-base"]
headers = {"Authorization": "Bearer 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"}
outputs=[]

def query(filename,model):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post("https://api-inference.huggingface.co/models/"+model, headers=headers, data=data)
    return response.json()
def createtable(outputs,models):
    # Create data for the table
    data = {
        "Model": models,
        "Output": outputs
    }

    # Convert to a DataFrame
    df = pd.DataFrame(data)

    # Display the table with custom styling
    st.markdown("""
    <style>
        .dataframe {
            border-collapse: collapse;
            width: 100%;
            text-align: center;
        }
        .dataframe td, .dataframe th {
            border: 2px solid #dddddd;
            padding: 8px;
            text-align: left;
        }
        .dataframe tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .dataframe tr:hover {
            background-color: #f1f1f1;
        }
        .dataframe th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

    # Render the table
    st.write(df.to_html(classes="dataframe", index=False), unsafe_allow_html=True)

def save_uploadedfile(uploadedfile):
    
    with open(os.path.join("", 'image.'+uploadedfiles.type[uploadedfiles.type.find('/')+1:]), "wb") as f:
        f.write(uploadedfile.getbuffer())
        st.image('image.'+uploadedfiles.type[uploadedfiles.type.find('/')+1:], caption="Selected image")
        outputs=[]
        for model in models:
            try:
                output = query('image.'+uploadedfiles.type[uploadedfiles.type.find('/')+1:],model)


            except:
                output = query('image.'+uploadedfiles.type[uploadedfiles.type.find('/')+1:],model)
            outputs.append(output[0]['generated_text'])
            

        createtable(outputs,models)
            # st.write(model,output[0]['generated_text'])
        # return st.success("Saved File:{} to Data".format('image.'+uploadedfiles.type[uploadedfiles.type.find('/')+1:]))

# st.text("A simple way to upload files directly into a directory")
# uploadedfiles = st.file_uploader("Upload PDF", type=["pdf"], accept_multiple_files=True)
uploadedfiles = st.file_uploader("Upload Image")

if uploadedfiles is not None:
    save_uploadedfile(uploadedfiles)
 


# Title for the app
