
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import uvicorn
import llm_utils
import os

#cors
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


#post request to initialize the api
@app.post("/init_api")
def init_api(session_token: str):
    llm_utils.init_client(session_token)
    return {"status": "initialized"}

@app.post("/send_message")
#message is text and attachment is a file uploaded to the server
def send_message(message: str, attachment: UploadFile = File(None)):
    #save file to server
    if attachment is not None:
        #get the file name
        file_name = attachment.filename
        #save the file
        with open(file_name, "wb") as buffer:
            buffer.write(attachment.file.read())
        #set the attachment to absolute path of the file pwd + file_name
        attachment = os.getcwd() + "/" + file_name
        print(message,attachment)
        response,conversation_id = llm_utils.send_message(message, attachment)
    else:
        response,conversation_id = llm_utils.send_message(message)
    if response is None:
        return{"response":"client is not initialized", conversation_id: None}
    return {"response": response, "conversation_id": conversation_id}

@app.post("/reset_conversation")
def reset_conversation():
    resp=llm_utils.reset_conversation()
    return {"status": resp}
if __name__ == "__main__":
    #run with debug mode on
    uvicorn.run(app, host="0.0.0.0", port=7000, log_level="debug")