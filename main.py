import logging
from typing import Text, Dict

import requests
from fastapi import FastAPI, Query, Header

from query import search_query, category_query, trending_query

app = FastAPI()
w_invitee: None

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=2,
    format="%(asctime)-15s %(levelname)-8s %(message)s"
)


@app.post("/search_stickers")
async def search_stickers(
        api_token: Text = Header(None, alias="api_token"),
        search_text=Query("happy", alias="search_text"),
        results_count=Query(1, alias="results_count")
) -> Dict:
    formatted_query = search_query.replace("search_text", search_text).replace("number_results", results_count)
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    url = "https://graph.snapchat.com/graphql"
    response = requests.post(url, json={"query": formatted_query}, headers=headers)
    sticker_json = {}
    json_response = response.json()
    if "data" in json_response:
        sticker_json = {
            "stickers": response.json()["data"]["sticker"]["searchStickers"]["stickerResults"]["items"]
        }
    else:
        sticker_json = json_response

    return sticker_json


@app.post("/stickers_by_category")
async def search_stickers(
        api_token: Text = Header(None, alias="api_token"),
        category_count=Query(1, alias="category_count"),
        results_count=Query(1, alias="results_count")
) -> Dict:
    formatted_query = category_query.replace("number_category", category_count).replace("number_results", results_count)
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    url = "https://graph.snapchat.com/graphql"
    response = requests.post(url, json={"query": formatted_query}, headers=headers)
    sticker_json = {}
    json_response = response.json()
    if "data" in json_response:
        sticker_json = {
            "stickers": response.json()["data"]["sticker"]["categoryStickers"]["stickerSection"]["stickerCategories"]
        }
    else:
        sticker_json = json_response

    return sticker_json


@app.post("/trending_stickers")
async def search_stickers(
        api_token: Text = Header(None, alias="api_token"),
        results_count=Query(1, alias="results_count")
) -> Dict:
    formatted_query = trending_query.replace("number_results", results_count)
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    url = "https://graph.snapchat.com/graphql"
    response = requests.post(url, json={"query": formatted_query}, headers=headers)
    sticker_json = {}
    json_response = response.json()
    if "data" in json_response:
        sticker_json = {
            "stickers": json_response["data"]["sticker"]["trendingStickers"]["stickerResults"]["items"]
        }
    else:
        sticker_json = json_response

    return sticker_json
