import requests
from django.conf import settings


def zpal_request_handler(
    merchant_id, amount, detail, user_email, user_phone_number, callback
):
    url = settings.ZARINPAL["gateway_request_url"]

    data = {
        "merchant_id": merchant_id,
        "amount": amount,
        "description": detail,
        "callback_url": callback,
        "email": user_email,
        "mobile": user_phone_number,
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    res = requests.post(url, json=data, headers=headers)
    res.raise_for_status()
    result = res.json()

    if result.get("data", {}).get("code") == 100:
        authority = result["data"]["authority"]
        payment_url = f"https://sandbox.zarinpal.com/pg/StartPay/{authority}"

        return payment_url, authority
    else:
        return None, None


def zpal_payment_checker(merchant_id, amount, authority):
    url = settings.ZARINPAL["gateway_verify_url"]

    data = {
        "merchant_id": merchant_id,
        "amount": amount,
        "authority": authority,
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    res = requests.post(url, json=data, headers=headers)
    res.raise_for_status()
    result = res.json()

    is_paid = result.get("data", {}).get("code") in [100, 101]
    ref_id = result.get("data", {}).get("ref_id", "")
    return is_paid, ref_id