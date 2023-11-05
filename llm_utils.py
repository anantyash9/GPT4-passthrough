from UnlimitedGPT import ChatGPT

api=None

#initialize client
def init_client(session_token):
    global api
    api = ChatGPT(
        session_token=session_token,
        clipboard_retrival=False, # WSL
        model=2 ,# GPT-4
        verbose=True,
    )

#send message
def send_message(message,attachment=None):
    if api is None:
        return None,None
    if attachment is None:
        x = api.send_message(
            message=message,
            input_mode="SLOW"
        )
        return x.response,x.conversation_id
    else:
        x = api.send_message(
            message=message,
            attachment=attachment,
            input_mode="SLOW"
        )
        return x.response,x.conversation_id
#reset conversation
def reset_conversation():
    if api is None:
        return None
    api.reset_conversation()
    return True

# init_client("eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..qf6ji9FKkK729oKH.u_rDzz1-LOunIy4n4Kg3BLFA7KnbSXN_Qzpn4EclFjqm3K2LW11NxCm-amultNzRoMWIa242_X6dROGuvmbEeCpkvbCtr2vBZ3yplwuDYUF6nT5iwNOgGXx1Oc9UNmz56rlYHxjQlzzRf2DV-TGBSQlkjMyHc5ovzxRD57Fhl3angUOwQbC6gC9p3-xzsi9XIyhvaToRsR28Q90CGBy042tiqN_D3zoa6pRYIRZCRRKa1BimzI7p9TQ06SQbhE8nvyWK6LjDvSXFGBPUOBmySC7yGOt5Os5-qys4UeKCZ002cuRU7uuSd6So10ENFk8gxbiwoPkx99vcWCrGbU8kgU1aWjkzGtLcd3Xyh3BuTNZNZoDs8JhbHVdDLEXCjtIpGvn5G8RnqEJQDNIjH_Ylf90WkvREgk1Vc8DPG0h1VBvZ4o_0-zupJDBOLUwSXv2pmwbXzQ3mvACdRu7Teu9ZSsZOQRh90nUI_s4MsT6RBo8gPsXNqff-LHr411vJd32p08jOPBJ4xwls5jrBKrbm7u16bLOv7YLjqSEmSrVcXNgFM5ag-YyIVsrh8RA4zyjhzMAIYuZbZMzWRK5sYk0VikQgu1SEbk4RxQjjZYFMkhZswk7rIfFYuC8Ji04hVxujU0F8ra-uoU6NvVrmEqdH8063epSWQhJnx4pCY_m_NgD2lNfv5VBDzf_eTgMMDCCmxGErYvkBl8e9EQiajYmMCCiG7LbcFKJlAaUjMEJQkt9Aner8RolL8nHtKpOsp-9tF5ecNVNdU0eTd6WnSseyd3JZMuDByP0iXcl_TFjevz3CTu3pbuzTpKnCH2igSlP7dcP9OQwp5b3dOcUVm4iNbMSGo7-sDlcxIQ0pDR3FpJvk8vy5TJB38n5ezTiDV50YIpkqf2U5grfz1hawdEb6S-yiKu6-dRa8zfAgdy5UT8QBj4r1HLj2Ivt7n9EYKs2EaCnAO6nbjUqawQtcEoky_myiHU2MhkKE5PlZ9PSOuhMvs6rpLbWhiClUM268dmSW8BasEHjxdey0KQkWEtl87ZgA9CLoZT5tGKKtPAtgABx_ZZWxi4rByBPPhkmBzLy1CUxy9gszroc7H1BOIQdyjQJfn7mv_GnjVccmyB4JX9pQ6lGxtHzRUH-teZs_nYa5odlqXUCWrN-au_-l3zH362Xjm7ytHN9eBWD-YiMr8qaWgY2X2zZnAF9cvF5FDojCe9JEnPkqxd6LyD_20DZIBqtxbDM-eaEogujWqrfl8YRQ75Ws8vx1PgnybBvtYkQeMHrLf-hNShMjniXV7oOAP6pEjnf8OvcfBDm7PH6tvpPUI_5HkGtrEg7RxLOTclaTLwwe-YrKTuBJoffG08XnBbBkbbxAfi1vHN8ashCZWjXqUF4RnXrBXhSVd2-WqHA6TUXp-vfrZxPKbcVd_A1w-LLp1xL5dktXTq828gfw0NvD03A5K8-FUnVtggVC5syFbbRpIDTy8zGgjQuzTfVZls4U02MLEYjKrsan-XfbdYos4qezz8Nt86uRsQhgDu7SErjNg35Gey31DNq-uLUJTIsAqyYS5VqAQvDG7KSC5UxEH0Eix_FV0_xK1EEIRmWQgYphdKVumEHBk6uuHS9TU_FjOP1XS7-6C9ACivKopPHI-UFaIcuVg3-k35QSaorlFjRHuaYzeBlg1CA0FQjHOMl2ZSXRkRSrWqqjwKilCjubf176FQkTjSMFnOTxQYFSzlIPHe6IVlb-4RsKUA65kSG7iMf8zfp9f0K5KZlQ1utNGMrjZp_ophscDmCLJzbmiONRNc2xGaPhGPxyLnbQOkOIcdTqqdEz2KeUmJLzotEX0Fpd5RKKoa1qOIKOcuvph0Zz_nf-mFI_n8w5RqnM8QKPsnojtTU2Rokj7vZYL_hntlfFeWHZUyPL5npwpwpF21I3FoPy7gbGl-pGYiGb1-lxEU6xrZ7Sb05A19oaSbbrfDTHdm_wcLIXM-T1KWlLZPLBq7uaL11J5vlUjyw5AWrR6982Eb-OO2i-1_vjC9WTHOkSlz6SsaAOuq8_2DIaXLQzeKGmZpqbZ5ILmz3hBz3aVxcGV0w5oaJlzH4dRH_V40W6-X7RWxeWgvByU4lWT368YpV0j0zTx6w_X300xd9e0B8Hebi_SoQlISZbTw9OIlNeqrWv_qKnprO_Fbvv0Jqs6O-n7Wvf9LQCMM5NSNtqeeZb6hE2A05mZomVgF7no4ov20i_5qxYSOGooj_B0DDzgISDz2QpyJndNparTlmk2r0NElgGcD4xC5BHFdsDr-gVIBATcM0zU4O-NoszIJLh1XsVrp04dvLKV3M0AiZx0I2fSEF9-UsfTSN7ltTNijqwChM755q3Fez5LNJWoh-4ccFX1kHfZXCn_YBDFsB6vkOT3bsPKSOvJ_8hIOyBHcfb0kH1YMJbtZajRcllRK3YgteyJWcwD9hyBTariy16AqC3_G8Efr7KCGjKWOcOQE6PuswQUXZzl0kslVvzLC2h_aGv3qTjBbJf-ET_-DFovKrnVYBFjQZ4_o2keQeRpjEmZjczpOS9EWVLmK3Zjf-m14ffjtQFB7hK--KmeGQLwNRZRiOwlodkJjFZi_2jp5S_Wa_5CZDP9H5vfN-zY1CtLa3HZfMBCZCiRQlnRBD51aT0_fBuNLyUn2lTW6hRqOOSFfTzc8o9KoQdnrjUehLCQdyJqS4Hqdw4BnFklFKNstd0c-I3EwcgJtyAaGjn3ufuDaAwy06kbCNSLtt_9-LjbU9GVEAhjQ5cER9nONx6cuUDpUeLdWhiA_JeraIbPh2tcw.NgFiPqR_ayQqQBZxhJklCg")
# print(send_message("Hello","/home/developer/workspace/GPT4-passthrough/router.jpg"))
