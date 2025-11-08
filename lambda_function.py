import json

def lambda_handler(event, context):
    try:
        # Get URL from POST body
        body = json.loads(event.get('body', '{}'))
        news_url = body.get('url')
        if not news_url:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing 'url'"})}

        # Mock summary instead of real API call
        summary = f"This is a mock summary for the article: {news_url}"

        return {"statusCode": 200, "body": json.dumps({"summary": summary})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
