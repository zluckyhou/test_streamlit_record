from st_audiorec import st_audiorec
import subprocess
import re
import streamlit as st
import os
import logging



# set logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# clear logger if exists
if logger.hasHandlers():
	logger.handlers.clear()

# create a console logger
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)



if "record_audio_data" not in st.session_state:
    st.session_state.record_audio_data = ''
if "audio_file" not in st.session_state:
	st.session_state.audio_file = ''


# wav_audio_data = st_audiorec()

# if wav_audio_data is not None:
#     st.audio(wav_audio_data, format='audio/wav')

with st.container(border=True):
	wav_audio_data = st_audiorec()

	output_path = 'record_audios'
	# remove directory if exists 
	# rm_user_directory = subprocess.run(["rm","-rf",output_path],check=True)
	# mkdir_user_directory = subprocess.run(["mkdir","-p",output_path],check=True)

	# output_file_path = os.path.join(output_path,"record_audio.mp3")
	
	logger.debug(f"record data: {wav_audio_data}")
	if wav_audio_data is not None:
		output_file_path = "record_audio.mp3"
		st.session_state.record_audio_data = wav_audio_data
		with open(output_file_path,'wb') as f:
			f.write(st.session_state.record_audio_data)		
		st.session_state.audio_file = output_file_path
		logger.info(f"audio file: {st.session_state.audio_file}")

if st.session_state.audio_file:
	st.markdown("display audio file")
	st.audio(st.session_state.audio_file)
	st.markdown("display audio data")
	st.audio(st.session_state.record_audio_data)
