import json
from datetime import datetime


def convert_to_millis(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def convertFromFormat1(jsonObject):
    return {
        "deviceId": jsonObject.get("deviceId"),
        "timestamp": convert_to_millis(jsonObject.get("timestamp")),
        "temperature": jsonObject.get("temperature"),
        "humidity": jsonObject.get("humidity")
    }


def convertFromFormat2(jsonObject):
    return {
        "deviceId": jsonObject.get("id"),
        "timestamp": jsonObject.get("time") * 1000,
        "temperature": jsonObject.get("temp"),
        "humidity": jsonObject.get("hum")
    }


def run_tests():
    with open("data-1.json") as f1, open("data-2.json") as f2, open("data-result.json") as fr:
        data1 = json.load(f1)
        data2 = json.load(f2)
        expected = json.load(fr)

        result1 = convertFromFormat1(data1)
        result2 = convertFromFormat2(data2)

        assert result1 == expected, "Format1 conversion failed"
        assert result2 == expected, "Format2 conversion failed"

        print("All tests passed ✅")


if __name__ == "__main__":
    run_tests()