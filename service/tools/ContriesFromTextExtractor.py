from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials


def extract(text, lang):
    if len(text) > 0:
        client = authenticate_client()
        text = clean_input_text(str(text))
        locations = []
        try:
            response = client.entities(documents=[prepare_documents(lang, text)]).documents[0]

            for entity in response.entities:
                if entity.type == "Location" and entity.name not in locations:  # and entity.sub_type == "GPE":
                    locations.append(entity.name)

        except Exception as err:
            print("Encountered exception. {}".format(err))
        return locations


def prepare_documents(lang, text):
    return {
        "id": "1",
        "language": "ar" if lang == "Arabic" else "en",
        "text": text
    }


def clean_input_text(text):
    return text \
        .replace("\\r", "") \
        .replace("\\n", "") \
        .replace("\\\\r", "") \
        .replace("\\\\n", "") \
        .replace("،", "") \
        .replace("\r\n", " ")


def authenticate_client():
    credentials = CognitiveServicesCredentials("3e9a99df8fdf48df81349ebfedf67748")
    text_analytics_client = TextAnalyticsClient(
        endpoint='https://eastus.api.cognitive.microsoft.com/',
        credentials=credentials)
    return text_analytics_client
