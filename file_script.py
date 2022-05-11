from pathlib import Path

exercises = [
    {
        "id": 74,
        "name": "Isometric Cervical Combination Strengthening in Sitting",
        "type": "NECK"
    },
    {
        "id": 530,
        "name": "Isometric Cervical Combination Strengthening in Standing",
        "type": "NECK"
    },
    {
        "id": 316,
        "name": "Cervical Flexion with Resistance Band in Sitting",
        "type": "NECK"
    },
    {
        "id": 317,
        "name": "Cervical Extension with Resistance Band in Sitting",
        "type": "NECK"
    },
]


def generate_kotlin_file():
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


def generate_swift_file():
    for exercise in exercises:
        exercise_number = exercise.get("id")
        name = exercise.get("name").title().replace(" ", "")
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