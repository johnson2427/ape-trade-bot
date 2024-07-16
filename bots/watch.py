from silverback import SilverbackApp


app = SilverbackApp()


@app.on_(my_contract.Received)
def toggle(log):
    pass
