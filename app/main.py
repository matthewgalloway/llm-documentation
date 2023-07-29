import logging
import streamlit as st
from streamlit_chat import message
from logger import logger



logger.info('Setting header...')
st.header("Lanchain help prompt")

logger.info('Preparing to receive input...')
prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if prompt:
    logger.info(f'Prompt received: {prompt}')
    with st.spinner("Generating response..."):
        logger.info('Generating response...')


