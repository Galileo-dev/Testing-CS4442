import openai
import os

class GPTParser:

    openai.api_key = os.environ.get('OPENAI_API_KEY')

    def data_extracter(response: str, delimiter: str):
        for i in range(len(response)):
            if response[i] == delimiter:
                for x in range(i+1, len(response)):
                    if response[x] == delimiter:
                        return response[i+1:x].lower()

    def datetime_parser(string: str):

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Transform the provided unparsed date and time into the format DD-MM HH:MM enclosed by % signs (time should be in 24 hour format). Respond only with the answer, no explanation."},
                {"role": "user", "content": string},
            ]
        )

        response = response.choices[0].message.content

        date = GPTParser.data_extracter(response, '%')

        return date

