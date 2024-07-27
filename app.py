# # import streamlit as st
# # import spacy
# # import os

# # # Adjust the path to point to the correct model directory
# # model_path = r"C:\Users\tomiw\OneDrive\Desktop\NER_MODEL\trained_ner_model"

# # # Print the contents of the model directory to verify
# # print("Contents of the model directory:", os.listdir(model_path))

# # # Load the trained SpaCy model
# # nlp = spacy.load(model_path)

# # st.title("NER Model with Streamlit")

# # text = st.text_area("Enter text for NER")

# # if text:
# #     doc = nlp(text)
# #     entities = [(ent.text, ent.label_) for ent in doc.ents]
# #     st.write(entities)




# import streamlit as st 
# from time import sleep
# from stqdm import stqdm # for getting animation after submit event 
# import pandas as pd
# from transformers import pipeline
# import json
# import spacy
# import spacy_streamlit



# def draw_all(
#     key,
#     plot=False,
# ):
#     st.write(
#         """
#         # NER Web App
        
        # This Named Entity Recognition Based Web App that can identify and classify text data.
        
#         This App is built using pretrained transformers which are capable of doing wonders with the Textual data.
        
#         ```
#          Named Entity Recognition
#         ```
#         """
#     )

    

# with st.sidebar:
#     draw_all("sidebar")



# def main():
#     st.title("NER Web App")
#     menu = ["Named Entity Recognition General",
#             "Named Entity Recognition Domain"]
#     choice = st.sidebar.selectbox("Choose Which model you want to use", menu)


#     if choice=="Named Entity Recognition General":

#         st.write("""
                 
                 
# Named Entity Recognition (NER) is a subfield of NLP and Artificial Intelligence (AI) that identifies and classifies named entities (such as person names, locations, organizations) in text, helping machines understand the context just like humans.
#         """)


        
#         nlp = spacy.load("C:/Users/tomiw/OneDrive/Desktop/NER_MODEL/your_model_directory")



#         st.subheader("Text Based Named Entity Recognition")
#         raw_text = st.text_area("Your Text","Enter Text Here")
#         if st.button("Analyze Text"):
#             if raw_text !="Enter Text Here":
#                 doc = nlp(raw_text)
#                 for _ in stqdm(range(50), desc="Please wait a bit. The model is     fetching the results !!"):
#                     sleep(0.1)
#                 spacy_streamlit.visualize_ner(doc, labels=nlp.get_pipe("ner").labels,   title= "List of Entities")













#     elif choice=="Named Entity Recognition Domain":
        
#         st.write("""
                 
#                 This is a Natural Language Processing (NLP) Based Web App that specializes in Named Entity Recognition (NER) for a specific domain.

#         """)
        
#         st.write("""
               
# Natural Language Processing (NLP) is a computational   technique to understand human language in the way it is   spoken and written.

#         """)
        
#         st.write("""
                 
                 
# Named Entity Recognition (NER) is a subfield of NLP and Artificial Intelligence (AI) that identifies and classifies named entities (such as person names, locations, organizations) in text, helping machines understand the context just like humans.
#         """)
        
        
#         st.image('qr_img.png')



# if __name__ == '__main__':
# #      main()import spacy

# import spacy

# def load_model(model_path):
#     try:
#         nlp = spacy.load(model_path)
#         print("Model loaded successfully")
#         return nlp
#     except Exception as e:
#         print(f"Error loading model: {e}")

# if __name__ == "__main__":
#     model_path = r"C:/Users/tomiw/OneDrive/Desktop/NER_MODEL/your_model_directory"
#     nlp = load_model(model_path)



import streamlit as st
import spacy
import time  # Import the time module
import spacy_streamlit

# Load your custom NER model
model_path = "C:/Users/tomiw/OneDrive/Desktop/NER_MODEL/your_model_directory"
nlp = spacy.load(model_path)

def main():
    st.title("Named Entity Recognition with spaCy")
    st.write("Enter text below and get named entity recognition results!")

    text_input = st.text_area("Text Input")

    if st.button("Analyze"):
        if text_input:
            with st.spinner('Analyzing...'):
                start_time = time.time()  # Record the start time
                try:
                    doc = nlp(text_input)
                    end_time = time.time()  # Record the end time
                    elapsed_time = end_time - start_time  # Calculate elapsed time

                    st.success(f"Processing completed in {elapsed_time:.2f} seconds")
                    st.write("Entities found:")
                    for ent in doc.ents:
                        st.write(f"{ent.text}, ({ent.label_})")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.write("Please enter some text for analysis.")

if __name__ == "__main__":
    main()





