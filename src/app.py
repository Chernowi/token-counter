import streamlit as st
import io
import os

# Import our custom modules
from file_handlers.pdf_handler import extract_text_from_pdf
from file_handlers.text_handler import extract_text_from_txt
from file_handlers.docx_handler import extract_text_from_docx
from utils.token_counter import count_tokens

def main():
    st.title("LLM Token Counter")
    st.write("Upload a document to count tokens according to different LLM tokenization schemes.")
    
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'txt', 'docx'])
    
    if uploaded_file is not None:
        file_details = {"Filename": uploaded_file.name, 
                       "FileType": uploaded_file.type, 
                       "FileSize": f"{uploaded_file.size / 1024:.2f} KB"}
        st.write(file_details)
        
        try:
            # Extract text based on file type
            if uploaded_file.name.endswith('.pdf'):
                text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.name.endswith('.txt'):
                text = extract_text_from_txt(uploaded_file)
            elif uploaded_file.name.endswith('.docx'):
                text = extract_text_from_docx(uploaded_file)
            else:
                st.error("Unsupported file format")
                return
            
            # Show text preview
            with st.expander("Text Preview"):
                st.text(text[:1000] + "..." if len(text) > 1000 else text)
            
            # Count tokens with different models
            models = ["simple", "gpt-3.5-turbo", "gpt-4", "claude", "llama"]
            token_counts = {}
            
            progress_bar = st.progress(0)
            for i, model in enumerate(models):
                with st.spinner(f"Counting tokens using {model} model..."):
                    token_counts[model] = count_tokens(text, model)
                progress_bar.progress((i + 1) / len(models))
            
            # Display token counts
            st.subheader("Token Counts by Model")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Simple Word Count", token_counts["simple"])
                st.metric("GPT-3.5-Turbo Tokens", token_counts["gpt-3.5-turbo"])
                st.metric("GPT-4 Tokens", token_counts["gpt-4"])
            
            with col2:
                st.metric("Claude Tokens (Approximated)", token_counts["claude"])
                st.metric("LLaMA Tokens", token_counts["llama"])
            
            # Create a bar chart for visualization
            st.subheader("Token Count Comparison")
            chart_data = pd.DataFrame({
                'Model': list(token_counts.keys()),
                'Token Count': list(token_counts.values())
            })
            st.bar_chart(chart_data, x='Model', y='Token Count')
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import pandas as pd
    main()