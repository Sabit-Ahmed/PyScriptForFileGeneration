import json
import requests
import numpy as np
from base64 import b64encode

def generate_ios_audio_file():
    instructions = np.unique([
        "LIFT HEAD AND ARMS UP",
        "BRING ARMS AT THE BACK",
        "BRING ARMS BACK FORWARD",
        "RETURN FLAT ON THE MAT",
        "RAISE YOUR RIGHT ARM AND YOUR LEFT LEG",
        "RAISE YOUR LEFT ARM AND YOUR RIGHT LEG",
        "LEFT",
        "RIGHT",
        "PULL AND SWING YOUR RIGHT HAND OUT TO THE RIGHT",
        "PULL AND AND SWING YOUR LEFT HAND OUT TO THE LEFT",
        "PULL AND SWING YOUR RIGHT HAND IN TO THE LEFT",
        "PULL AND SWING YOUR LEFT HAND IN TO THE RIGHT",
        "RETURN TO THE STARTING POSITION",
        "BEGIN",
        "BRING YOUR LEFT ELBOW TO YOUR RIGHT KNEE",
        "BRING YOUR RIGHT ELBOW TO YOUR LEFT KNEE",
        "BEND YOUR KNEES",
        "SWITCH YOUR LEFT FOOT WITH YOUR RIGHT FOOT",
        "PLACE YOUR RIGHT FOOT ON THE SEAT",
        "PLACE YOUR LEFT FOOT ON THE SEAT",
        "BEND YOUR LEFT ELBOW",
        "BEND YOUR RIGHT ELBOW",
        "RAISE YOUR RIGHT ARM",
        "RAISE YOUR LEFT ARM"
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
        data = respose.json()
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

