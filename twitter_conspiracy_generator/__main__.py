import os
import random
from typing import Any

import httpx
from dotenv import load_dotenv
from lxml import html
from openai import OpenAI
from twitter_conspiracy_generator.twitter import post_conspiracy_theory

load_dotenv(".env")

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

urls_with_headlines = [
    "https://www.bbc.com/",
    "https://www.bbc.com/news",
    "https://www.bbc.com/sport",
    "https://www.bbc.com/innovation",
    "https://www.bbc.com/culture",
    "https://www.bbc.com/travel",
    "https://www.bbc.com/future-planet",
]


def get_headlines() -> list[str]:
    headlines = []

    for url in urls_with_headlines:
        with httpx.Client() as httpx_client:
            homepage_response = httpx_client.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                },
            )
            # load html response into a tree
            root = html.fromstring(homepage_response.text)

            tmp_headlines = root.xpath(
                "//h2[contains(@data-testid, 'card-headline')]//text()"
            )

            print(f"Headlines fetched from {url}. Count: {len(tmp_headlines)}")

            for item in tmp_headlines:
                headlines.append(item)

    print(
        f"Headlines fetched successfully! Total Count: {len(headlines)}. Selecting 1 random headlines."
    )

    return random.choices(headlines, k=1)


def generate_conspiracy_prompt(headline) -> dict[str, str]:
    print("Generating conspiracy prompt")
    return {
        "role": "user",
        "content": f"""You will be given a headline from a news website.
            Your task is to create an insanely believable, satire and entertaining conspiracy theory from the headline. 

            Guidelines:
            - Your response should be solely the conspiracy theory without any introduction or conclusion.
            - DO NOT USE ANY HASHTAGAS!
            - Write in B1 level English.
            - Be creative and think outside the box.
            - Do not include any war related content.
            - Ignore all political events and focus on the headlines only.
            - First sentence should be catchy and intriguing, inviting the reader to read more.
            - Headline should be visible in the generated text.

            Headline: {headline}.""",
    }


def generate_conspiracy(conspiracy_prompt: dict[str, str]) -> Any:
    print("Generating conspiracy theory")
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "I respond in messages that are 230 characters or less. Otherwise i will be penalized.",
            },
            conspiracy_prompt,
        ],
    )


def add_hashtags_to_conspiracy(conspiracy_theory: str) -> Any:
    print("Adding hashtags to conspiracy theory")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": (
                    "Please modify the following text by turning people, places, events, "
                    "and other key terms into hashtags. Integrate these hashtags directly after "
                    "the relevant words within the sentence, without clustering them at the "
                    "beginning or end. Maintain the natural flow and readability of the original message.\n\n"
                    f"Original message: {conspiracy_theory}."
                ),
            },
        ],
    )
    return completion.choices[0].message.content


headlines = get_headlines()

conspiracies = [
    add_hashtags_to_conspiracy(
        generate_conspiracy(generate_conspiracy_prompt(headline))
        .choices[0]
        .message.content
    )
    for headline in headlines
]

for conspiracy in conspiracies:
    post_conspiracy_theory(conspiracy)
