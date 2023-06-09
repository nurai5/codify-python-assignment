from decouple import config
import openai


def complete_prompt(prompt):
    openai.api_key = config('OPENAI_API_KEY')

    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
    )

    return response.choices[0].prompt_message.strip()
