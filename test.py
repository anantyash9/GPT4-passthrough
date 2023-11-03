from UnlimitedGPT import ChatGPT

session_token = ""

api = ChatGPT(
    session_token=session_token,
    clipboard_retrival=False, # WSL
    model=2 # GPT-4
)

x = api.send_message(
    message="Describe this image.",
    attachment="/app/DJI_0005.png",
    input_mode="SLOW"
)

print(x.response)