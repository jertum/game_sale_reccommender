import httpx

# using httpx directly
response = httpx.get(url="https://isthereanydeal.com/game/clair-obscur-expedition-33/history/#price-chart:detail")

# create a configurable client
client = httpx.Client(
    http2 = True,
    follow_redirects = True,
    headers = {
        "user-agent": "jt"
    }
)
response2 = client.get(url="https://isthereanydeal.com/game/clair-obscur-expedition-33/history/#price-chart:detail")

print(response.status_code)
print(response2.status_code)

print(response.text)
print(response2.text)