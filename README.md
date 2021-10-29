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
- Go to your app, your screen will look like below

