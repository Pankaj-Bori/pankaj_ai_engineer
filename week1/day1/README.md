# Day 1: First Groq API Request

This project demonstrates how to send a prompt to a Groq language model using
the Groq Python SDK.

## What This Project Does

The program:

- Loads the Groq API key from a `.env` file
- Creates a Groq client
- Sends one prompt to the `openai/gpt-oss-20b` model
- Prints the complete API response
- Prints the assistant's response separately

## Requirements

- Python 3.14 or later
- `uv`
- A Groq API key

## Installation

Open PowerShell in the `day1` directory and install the dependencies:

```powershell
uv sync
