import json
import requests
import numpy as np
from base64 import b64encode

def generate_ios_audio_file():
    instructions = np.unique([
        "LIFT LEFT LEG UP",
        "LIFT RIGHT LEG UP"
    ])

    # instructions = [" ".join(x.split("_")) for x in instructions]

    AUTHORIZATION = f"vauser:YWlhaYTRcGl1SuNaN2VyOiQkTUYTERMDIw".encode()

    for x in instructions:
        filename = "_".join([i.lower() for i in x.split(" ")]) + ".wav"

        respose = requests.post(
            url="https://devvaapi.injurycloud.com/api/voice/generate",
            json={
                "Tenant": "dev",
                "VoiceText": x
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Basic {str(b64encode(AUTHORIZATION))[2:-1]}",
            }
        )
        data = json.loads(respose.json())
        resp = requests.get(data["Message"]["AudioUrl"])
        with open("audio_cues/" + filename, "wb") as file:
            file.write(resp.content)

    for x in instructions:
        name = "_".join(x.split())
        print(f"static let {name} = \"{' '.join([i.lower() for i in x.split()])}\"")

    print()

    for x in instructions:
        x = x.split(" ")
        name = x[0].lower() + "".join([i.title() for i in x[1:]])
        print(f"static private let {name} = try? AVAudioPlayer(contentsOf: URL(fileURLWithPath: Bundle.main.path(forResource: \"{'_'.join([i.lower() for i in x])}\", ofType: \"wav\")!))")

