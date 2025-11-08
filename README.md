# NewsSummarizerAPI

This is a simple AWS Lambda function connected to API Gateway that summarizes news articles.  
Currently, it uses a **mock summary** instead of calling an actual AI API, so it works instantly without external API keys.

---

## Endpoint

POST https://ujmlu3om96.execute-api.ap-south-1.amazonaws.com/prod/summarize

yaml
---
## Request

Send a JSON body with the URL of the news article you want to summarize:

```json
{
  "url": "https://www.bbc.com/news/world-66753499"
}

Response
The Lambda function returns a JSON response with a mock summary:
json

{
  "summary": "This is a mock summary for the article: https://www.bbc.com/news/world-66753499"
}


Usage
Open a terminal or Postman.
Make a POST request to the API endpoint.
Include the Content-Type: application/json header.
Send a JSON body with the news article URL.
The API returns a mock summary.

Notes
This version does not call the real OpenAI or Hugging Face API; it only returns a placeholder summary.
To integrate with a real API, replace the mock summary code in lambda_function.py with actual API calls.


