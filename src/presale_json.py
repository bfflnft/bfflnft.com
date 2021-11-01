import json

LINK_BASE = "json/"
LINK_IPFS = "ipfs://QmX8JQRxyNbU98xSey3hCiBb6z7BXZdowWA8ihgPxDAUEM"
AMOUNT = 100

for n in range(AMOUNT):
    data = {
        "name": f"{n+1}",
        "image": LINK_IPFS + f"/{n+1}.png",
    }

    current = n + 1
    with open(LINK_BASE + f"{n+1}.json", 'w') as f:
        json.dump(data, f, indent=2)