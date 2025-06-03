from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

mock_data = {
    "2025-06-01": {
        "buy_alerts": ["NLIC", "HDL", "NABIL"],
        "sell_alerts": ["PRVU", "MLBBL", "NRIC"]
    },
    "2025-05-31": {
        "buy_alerts": ["NRIC", "NTC", "SHIVM"],
        "sell_alerts": ["NABIL", "PRVU", "HDL"]
    }
}

@app.get("/alerts/today")
def get_today_alerts():
    today = datetime.now().strftime("%Y-%m-%d")
    return {"date": today, **mock_data.get(today, {"buy_alerts": [], "sell_alerts": []})}

@app.get("/alerts/yesterday")
def get_yesterday_alerts():
    return {"date": "2025-05-31", **mock_data.get("2025-05-31", {"buy_alerts": [], "sell_alerts": []})}
