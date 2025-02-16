# Verse of the Day Bot

This bot automatically posts a daily Bible verse to your Instagram page.

## Features

- Fetches the daily verse image from Olive Tree Bible Software.
- Posts the image to Instagram with a caption.
- Runs daily at 05:00 AM IST using GitHub Actions.

## Prerequisites

- Python 3.9 or higher
- Poetry for dependency management
- An Instagram account
- GitHub repository secrets for Instagram credentials

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/verse-of-the-day-bot.git
   cd verse-of-the-day-bot
   ```

2. Install dependencies using Poetry:

   ```sh
   poetry install
   ```

3. Create a `.env` file in the root directory and add your Instagram credentials:
   ```env
   INSTAGRAM_USERNAME=your_instagram_username
   INSTAGRAM_PASSWORD=your_instagram_password
   ```

## Usage

To run the bot locally, execute:

```sh
poetry run python source/post_image.py
```

## GitHub Actions

The bot is configured to run daily at 05:00 AM IST using GitHub Actions. Ensure you have set up the following secrets in your GitHub repository:

- `INSTAGRAM_USERNAME`
- `INSTAGRAM_PASSWORD`

The workflow file is located at `.github/workflows/post_image.yml`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
