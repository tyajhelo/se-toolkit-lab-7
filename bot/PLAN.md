# Development Plan

The goal of this project is to build a Telegram bot with a clean architecture that separates command handling logic from the Telegram transport layer. The bot will be structured so that all handlers are simple Python functions that take a string input and return a string output. This allows testing the bot without needing Telegram.

The first step is to scaffold the project structure inside the bot directory. This includes creating the entry point (bot.py), handler modules, configuration file, and dependency file. The bot will support a CLI test mode using the --test flag, which allows commands to be executed locally.

In the second stage, the bot will integrate with the backend API using LMS_API_KEY and LMS_API_BASE_URL. Services will be added to fetch data from endpoints like /items and /analytics.

In the third stage, the bot will support natural language input using an LLM. The bot will route user input either to handlers or to the LLM.

Finally, the bot will be deployed and connected to Telegram using BOT_TOKEN, while preserving the same handler logic.
