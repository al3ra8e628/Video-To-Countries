import os

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from geopy.geocoders import Nominatim
from msrest.authentication import CognitiveServicesCredentials

geolocation = Nominatim(user_agent="video-to-countries")

AZURE_TEXT_ANALYTICS_SUBSCRIPTION_KEY = os.getenv("AZURE_TEXT_ANALYTICS_SUBSCRIPTION_KEY")
AZURE_TEXT_ANALYTICS_SUBSCRIPTION_REGION = os.getenv("AZURE_TEXT_ANALYTICS_SUBSCRIPTION_REGION")


def extract(text, lang):
    countries = []
    if len(text) > 0:
        client = authenticate_client()
        text = clean_input_text(str(text))
        try:
            response = client.entities(documents=[prepare_documents(lang, text)]).documents[0]
            for entity in response.entities:
                if entity.type == "Location":
                    handle_location(countries, entity, lang)
        except Exception as err:
            print("Encountered exception. {}".format(err))

    return countries


def handle_location(countries, entity, lang):
    location_country = location_to_country(entity.name, get_language_code(lang))
    if location_country is not None and \
            location_country not in countries:
        countries.append(location_country)


def location_to_country(query, language):
    country = None
    location = geolocation.geocode(
        query=query,
        language=language
    )

    if location is not None:
        if location.raw["type"] == "city" or \
                location.raw["class"] == "boundary":
            address_elements = str(location.raw["display_name"]).strip().split(",")
            country = address_elements[-1].strip()
    return country


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


def get_language_code(language):
    return "en" if language == "English" else "ar"


def authenticate_client():
    credentials = CognitiveServicesCredentials(AZURE_TEXT_ANALYTICS_SUBSCRIPTION_KEY)
    text_analytics_client = TextAnalyticsClient(
        endpoint='https://' + AZURE_TEXT_ANALYTICS_SUBSCRIPTION_REGION + '.api.cognitive.microsoft.com/',
        credentials=credentials)
    return text_analytics_client
