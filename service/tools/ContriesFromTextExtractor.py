from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

credential = AzureKeyCredential("3e9a99df8fdf48df81349ebfedf67748")
endpoint = "https://eastus.api.cognitive.microsoft.com/"


def extract(text):
    text = str(text)
    text_analytics_client = TextAnalyticsClient(endpoint, credential)
    print("NER process started on the following text: " + text)

    lower = text \
        .replace("\\r", "") \
        .replace("\\n", "") \
        .replace("\\\\r", "") \
        .replace("\\\\n", "") \
        .lower()

    result = text_analytics_client.recognize_entities(documents=[lower])[0]

    locations = []

    for entity in result.entities:
        if entity.category == 'Location' and entity.text not in locations:
            locations.append(entity.text)

    return locations
