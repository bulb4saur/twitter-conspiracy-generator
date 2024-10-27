# 🛸 Twitter conspiracy Generator 🤖

Welcome to **Twitter conspiracy Generator** - the project you never asked for but definitely need! This Python-powered bot scrapes news headlines, feeds them to ChatGPT, and generates the wildest, most unhinged conspiracy theories. Oh, and did I mention it tweets them for the world to enjoy? 🌍✨

## 🚀 Features

- **Scrapes news headlines** from popular sources (starting with the BBC).
- **Generates mind-bending conspiracy theories** using OpenAI's ChatGPT.
- **Tweets conspiracies** in perfectly chunked, threaded madness.
- **Uses cutting-edge Python libraries** like `HTTPX`, `LXML`, `Tweepy`, and `OpenAI`.

## 📖 How It Works

1. **Scrape Headlines**: The bot scrapes juicy news headlines from various categories (news, sports, etc.) using `HTTPX` and `LXML`.
2. **Generate Conspiracies**: ChatGPT transforms those headlines into full-blown tinfoil-hat conspiracies.
3. **Tweet It**: The conspiracy is broken into bite-sized tweets and threaded together for Twitter glory.

## 🔧 Setup

We use Poetry to manage dependencies. Install Poetry if you haven’t already.

```bash
poetry install
```

Add Your API Keys
Make sure you have your API keys ready for:
- Twitter API (Tweepy)
- OpenAI API

Then, add them to a .env file.

```env
OPENAI_API_KEY=#

TWITTER_API_KEY=#
TWITTER_API_KEY_SECRET=#

TWITTER_ACCESS_TOKEN=#
TWITTER_ACCESS_TOKEN_SECRET=#
```

## 🚀 Run the Bot

```bash
poetry run python twitter-conspiracy-generator
```

Sit back and watch as your bot generates chaos, one tweet at a time. 🌪️

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👽 Contribute

Got ideas for even crazier conspiracies? Fork the repo and submit a PR! Or just open an issue and tell me what you think.

## 🔮 Follow the Madness
- Follow the bot on Twitter: [@fake_the_garlic](https://x.com/fake_the_garlic)
- Join our Discord: [Community](https://discord.gg/vfT9VCNTwp)

## Disclaimer: 

All conspiracies generated are for entertainment purposes only. Any resemblance to actual conspiracies is purely coincidental. 😉
