# README

Scrapes all the target items listed in `targets.csv` and save the JSON API response in the `data` folder. The data can be visualised later for consumption.

Currently only supports scraping Shopee items.

## How to run

This project uses the [Poetry](https://python-poetry.org) to manage its dependencies. Please refer to the guide for the [installation steps](https://python-poetry.org/docs/#installation).

After Poetry is installed, run the following commands:

```
poetry install # install Python dependencies

poetry run python scrape.py # run the script from virtualenv
```

The script will generate a JSON file for each row in `targets.csv` with file name in format `{itemid}-{shopid}.json`.

## FAQ

### What is itemid and shopid?

Need to be manually fetched from the HTTP response in the browser when navigating to the item page through the developer console.

## TODOs

- [ ] add manually-triggered Github Action workflow to add new item to `targets.csv`, fetching the `itemid` and `shopid` automatically
