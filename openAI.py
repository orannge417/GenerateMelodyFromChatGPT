# Cannot execute this program as gpt-4 is not publically useful (waiting for queue)

import openai


def getResponse():
    openai.api_key="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"
    modelName = "gpt-4"

    prompt = 'Generate a graduation song with four sentences . Please output the Melody in ABC notation, with the lyrics for each note are included in quotation marks after the note (e.g., /From/ + C |)'


    response = openai.ChatCompletion.create(
        model = modelName,
        messages = [
            {"role" : "user", "content" : prompt},
        ],
    )

    print(response.choices[0]["message"]["content"])
