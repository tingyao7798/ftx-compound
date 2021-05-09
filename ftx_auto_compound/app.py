import json
from ftx import FtxClient
import secrets
import os

# Set aws secret name and ftx subaccount name if any


SECRET_NAME = os.environ.get("SECRET_NAME")
SUBACC_NAME = os.environ.get("SUBACC_NAME")


def lambda_handler(event, context):
    secret_keypair = secrets.get_secret(SECRET_NAME)
    key = list(secret_keypair.keys())[0]
    secret = secret_keypair[key]

    if not SUBACC_NAME:
        print("Using main account credentials...")
        ftx = FtxClient(api_key=key, api_secret=secret)
    else:
        print("Using subaccount credentials...")
        ftx = FtxClient(api_key=key, api_secret=secret, subaccount_name=SUBACC_NAME)
    bal_resp = ftx.get_balances()

    print("Getting latest balances", bal_resp)

    for balance in bal_resp:
        if balance["coin"] == "USD":
            coin = balance["coin"]
            size = balance["total"]

    lend_resp = ftx.submit_lending_offer(coin=coin, size=size, rate=0.00001)
    print("Submitted lending offer", lend_resp)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": f"${size} {coin} @ 0.00001 lending offer submitted "}
        ),
    }
