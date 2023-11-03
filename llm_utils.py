from UnlimitedGPT import ChatGPT

api=None

#initialize client
def init_client(session_token):
    global api
    api = ChatGPT(
        session_token=session_token,
        clipboard_retrival=False, # WSL
        model=2 # GPT-4
    )

#send message
def send_message(message,attachment=None):
    if api is None:
        return "Please initialize the client first"
    x = api.send_message(
        message=message,
        attachment=attachment,
        input_mode="SLOW"
    )
    return x.response
