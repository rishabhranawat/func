import os
from newsapi import NewsApiClient

NEWS_API_KEY = os.environ['NEWS_API_KEY']
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def get_news_about_a_topic(topic, from_param, language):
	all_articles = newsapi.get_everything(q=topic,
										  from_param='2023-10-04',
										  language='en',
										  sort_by='relevancy',
										  page=2)

	response = []
	for article in all_articles:
		constructed_content = article["title"] + " " + article["description"] + " " + article["content"]
		doc = {
			"title": article["title"],
			"url": article["url"],
			"content": constructed_content,
			"source": article["source"]["name"],
			"date": article["publishedAt"],
		}
		response.append(doc)
	return response

def funcs():
	functions = [
			{
			"name": "get_news_about_a_topic",
			"description": "Gets news articles about a provided topic",
			"parameters": {
				"type": "object",
				"properties": {
					"topic": {
						"type": "string",
						"description": "Topic that we want to learn about",
					},
					"from_param": {
						"type": "string",
						"description": "Starting date in the format: YYYY-MM-DD",
					},
					"language": {
						"type": "string",
						"description": "Language code in the ISO 639 format"
					}
				},
				"required": ["topic", "from_param", "language"],
			},
		}
	]
	return functions