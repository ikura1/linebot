import os

import linebot
from linebot.models import ImageSendMessage, TextSendMessage

from weather import Weather


LINE_ID = os.getenv("LINE_ID")
LINE_TOKEN = os.getenv("LINE_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")


def main():
    bot = linebot.LineBotApi(LINE_TOKEN)
    # message = TextSendMessage(text="hoge")
    w = Weather(WEATHER_TOKEN)
    response = w.get_weather_by_city_name("Osaka")
    json = response.json()
    icon_id = json["weather"][0]["icon"]
    icon_url = w.get_icon(icon_id).url

    message = ImageSendMessage(
        original_content_url=icon_url, preview_image_url=icon_url
    )
    try:
        bot.push_message(LINE_ID, message)
    except linebot.exceptions.LineBotApiError as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error.message)
        print(e.error.details)


if __name__ == "__main__":
    main()