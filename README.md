<p align="center"><img src="https://user-images.githubusercontent.com/57827233/139462786-6dc7d06b-fe57-4343-8a15-3222e1f099b5.png" width="120"></p>
<h1 align="center">Sticker kit REST API</h1>
<p align="center">Simplified REST API to get stickers from Snap</p>

# 💻 Instructions
## Search stickers
- Request:
```python
url = "https://sticker-kit-horizon733.cloud.okteto.net?search_text=morning&results_count=1"
headers = {"api_token": f"Bearer {your-api-token}"}
requests.post(url=url, headers=headers)
```
- Reponse:
```json
{
    "stickers": [
        {
            "itemType": "SNAPCHAT_STICKERS",
            "id": "AdUq16II9jTD",
            "pngURL": "https://bolt-gcdn.sc-cdn.net/3/dRORxCGc9jycqgwaRIXoH?bo=EiIaABoAMgF9OgsEBQcNDxFydHZ3e0IGCNSV5usFSAJQB2AB&uc=7&appID=00f481a8-6716-4af7-ad1c-8a35cd6e00fb&sessionID=c6ca4264-e12d-4a23-9535-68b9e89829e7",
            "thumbnailURL": "https://bolt-gcdn.sc-cdn.net/3/dRORxCGc9jycqgwaRIXoH?bo=EiIaABoAMgF9OgsEBQcNDxFydHZ3e0IGCNSV5usFSAJQB2AB&uc=7&appID=00f481a8-6716-4af7-ad1c-8a35cd6e00fb&sessionID=c6ca4264-e12d-4a23-9535-68b9e89829e7"
        }
    ]
}
```
## Get Trending Stickers
- Request:
```python
url = "https://sticker-kit-horizon733.cloud.okteto.net/trending_stickers?results_count=1"
headers = {"api_token": f"Bearer {your-api-token}"}
requests.post(url=url, headers=headers)
```
- Reponse:
```json
{
    "stickers": [
        {
            "id": "AS0b8vs3e90T",
            "pngURL": "https://bolt-gcdn.sc-cdn.net/3/oirSJQJYAe0DAGwpOnWFq?bo=EiIaABoAMgF9OgsEBQcNDxFydHZ3e0IGCPGJ_PIFSAJQB2AB&uc=7&appID=00f481a8-6716-4af7-ad1c-8a35cd6e00fb&sessionID=1de85c89-aefd-4dcd-89d1-fa536242faad",
            "thumbnailURL": "https://bolt-gcdn.sc-cdn.net/3/oirSJQJYAe0DAGwpOnWFq?bo=EiIaABoAMgF9OgsEBQcNDxFydHZ3e0IGCPGJ_PIFSAJQB2AB&uc=7&appID=00f481a8-6716-4af7-ad1c-8a35cd6e00fb&sessionID=1de85c89-aefd-4dcd-89d1-fa536242faad"
        }
    ]
}
```

## Search Stickers by Category
- Request:
```python
url = "https://sticker-kit-horizon733.cloud.okteto.net/stickers_by_category?results_count=1&category_count=1"
headers = {"api_token": f"Bearer {your-api-token}"}
requests.post(url=url, headers=headers)
```
- Reponse:
```json
{
    "stickers": [
        {
            "category": "Hi",
            "stickerResults": {
                "items": [
                    {
                        "itemType": "SNAPCHAT_STICKERS",
                        "id": "Ab0LnHrGa3Iv",
                        "pngURL": "https://bolt-gcdn.sc-cdn.net/3/4mpR7vl6N2m7JJ01iwhVc?bo=EiIaABoAMgF9OgsEBQcNDxFydHZ3e0IGCPSm5usFSAJQB2AB&uc=7&appID=00f481a8-6716-4af7-ad1c-8a35cd6e00fb&sessionID=889a68a5-7ebc-4d84-9090-ffe1d949caf2",
                        "thumbnailURL": "https://bolt-gcdn.sc-cdn.net/3/4mpR7vl6N2m7JJ01iwhVc?bo=EiIaABoAMgF9OgsEBQcNDxFydHZ3e0IGCPSm5usFSAJQB2AB&uc=7&appID=00f481a8-6716-4af7-ad1c-8a35cd6e00fb&sessionID=889a68a5-7ebc-4d84-9090-ffe1d949caf2"
                    }
                ]
            }
        }
    ]
}
```

## How to get API Token
- Go to your app, your screen will look like below.
<img src="https://user-images.githubusercontent.com/57827233/139457181-683b8baf-ca3f-49d2-a972-8e98033b81d6.png">

- Now, Click on Initial Version, Make sure `Enable` Sticker Kit. It will look like below
<img src="https://user-images.githubusercontent.com/57827233/139458516-a427412d-82f0-4302-bedb-98eae427d2ec.png">

- Go back to Setup, and Scroll down, you will be able to `API Tokens` copy whichever you want to, 
  make sure your App is in that Active on that Stage. API Token will look like below.
<img src="https://user-images.githubusercontent.com/57827233/139459155-e5e0b4be-3183-4ab9-90d8-7f92187e150b.png">

# How to Contribute?
- Make sure to Read Code of Conduct.
- Help me to test it with every case, to check it works and doesn't crash.
- Update Code? Sure, If you find anything helpful to be added please. FYI: This is made just to simplify work of Developers of other languages.



