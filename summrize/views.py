from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests 
from openai import OpenAI
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GENAI_API_KEY"))



@api_view(['POST'])
def message(request):

    data = request.data   # request body
    message = data['message']
    client = OpenAI(
    api_key=groq_api,
    base_url="https://api.groq.com/openai/v1",
    )

    summrize_response = client.responses.create(
        input=message,
        model="openai/gpt-oss-20b",
    )
    print("summrize",summrize_response.output_text)

    # model = genai.GenerativeModel("gemini-1.5-flash")
    model = genai.GenerativeModel("gemini-2.5-flash")
    # model = genai.GenerativeModel("gemini-1.0-pro")
    answser_response = model.generate_content(message)

    print("answer",answser_response.text)
    return Response({
        "data": message,
        "summary": summrize_response.output_text,
        "answer":answser_response.text
    })
