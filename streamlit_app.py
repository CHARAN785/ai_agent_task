import streamlit as st
from agent import generate_agent_response

st.title("Autonomous AI Document Agent")

user_request = st.text_area("Enter your request")

if st.button("Generate Document"):
    if user_request.strip():
        with st.spinner("Agent is planning and generating document..."):
            result = generate_agent_response(user_request)

        st.success("Document generated successfully")

        st.subheader("Agent Plan")
        st.write(result["agent_plan"])

        st.subheader("Document Title")
        st.write(result["document_title"])

        st.subheader("Generated Content")
        st.write(result["document_content"])

        st.subheader("File Path")
        st.write(result["file_path"])
    else:
        st.warning("Please enter a request")