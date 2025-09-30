from google import genai


class GeminiChat:

    def chat(self):
        client = genai.Client()
        response = client.models.generate_content(
            model="",
            contents=""
        )
        print(response.text)
