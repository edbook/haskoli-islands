import json
import logging
import sys
from pathlib import Path

from .utils import configure_logger

logger = configure_logger(__name__)
# Look up icelandic searchterm 'word' in the dictionaries 'minstae' and 'binstae'
# and return a dict containing the english and icelandic citation forms of the word.
base_dir = Path(__file__).parent.resolve().parent.parent.parent
data_file = base_dir / "data" / "minstae.json"
minstae_data = json.loads(data_file.read_text())

data_file = base_dir / "data" / "binstae.json"
binstae_data = json.loads(data_file.read_text())


def lookup(word):
    word = word.lower()
    # If 'word' is in citation form, look up in 'minstae' returns the translation.
    try:
        entry = minstae_data[word]
        entry["isTerm"] = word
        return entry
    # If 'word' is not found in 'minstae', it may not be in citation form and a
    # look up in 'binstae' is performed instead.
    except KeyError:
        try:
            entry = binstae_data[word]
            return entry
        # If 'word' is not found in 'binstae', the look-up has failed and an empty
        # dict is returned.
        except KeyError:
            logger.error(f"{word} was not found in any vocabulary")
            return {}
