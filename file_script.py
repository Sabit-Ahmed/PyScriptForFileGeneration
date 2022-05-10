from pathlib import Path

exercises = [
    {
        "id": 678,
        "name": "OneLeggedHingeRightInStanding",
        "type": "golf"
    },
    {
        "id": 652,
        "name": "OneLeggedSquats",
        "type": "fitness"
    },
    {
        "id": 621,
        "name": "SwimmerInProne",
        "type": "golf"
    },
]


def generate_android_file():
    for exercise in exercises:
        exercise_number = exercise.get("id")
        name = exercise.get("name")
        category = exercise.get("type").lower()

        folder = Path() / category
        if not folder.exists():
            folder.mkdir()

        print(f"{name}(context),")

        with open(f"{folder}/{name}.kt", "w") as file:
            file.write(f"""package org.tensorflow.lite.examples.poseestimation.exercise.home.{category}

    import android.content.Context
    import org.tensorflow.lite.examples.poseestimation.exercise.home.HomeExercise

    class {name}(context: Context) : HomeExercise(context = context, id = {exercise_number})""")


def generate_ios_file():
    for exercise in exercises:
        exercise_number = exercise.get("id")
        name = exercise.get("name")
        category = exercise.get("type").lower()

        folder = Path() / category
        if not folder.exists():
            folder.mkdir()

        print(f"{name}(),")

        with open(f"{folder}/{name}.swift", "w") as file:
            file.write(f"""import Foundation

final class {name}: HomeExercise {{

    override init() {{
        super.init()
        self.id = {exercise_number}
    }}

}}""")