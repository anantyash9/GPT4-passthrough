FROM ultrafunk/undetected-chromedriver

# updatet chrome
RUN apt update -y && apt install -y google-chrome-stable

# update undetected chromedriver
RUN pip install -U git+https://github.com/ultrafunkamsterdam/undetected-chromedriver


# copy the contents of UnlimitedGPT folder to /app/UnlimitedGPT
COPY UnlimitedGPT /app/UnlimitedGPT

# set the working directory to /app/UnlimitedGPT
WORKDIR /app/UnlimitedGPT

# install the requirements
RUN pip install -r requirements.txt

#install the python packages
RUN pip install .


#copy test.py to app
COPY server.py /app

#copy DJI_0005.png to app
COPY llm_utils.py /app

#set the current working directory to /app
WORKDIR /app


#run forever so i can connect to it
# CMD ["tail", "-f", "/dev/null"]
#install fastapi, uvicorn,python-multipart
RUN pip install fastapi uvicorn python-multipart

#run the test.py
CMD ["python", "server.py"]


#command to check chrome version
#RUN chromium-browser --version