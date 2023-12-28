import tomllib
import json
import datetime
from mastodon import Mastodon


def datetime_serializer(obj):
    """Basic serializer for datetime objects."""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def write_account_data(account):
    """Write account data to file."""
    with open(f'output/{account.username}.json', 'w') as f:
        f.write(json.dumps(account, default=datetime_serializer, indent=4))


def post_msg(client, msg):
    client.toot(msg)


def main(config):
    mastodon_client = create_poster_client(config)
    post_msg(mastodon_client, 'API POSTER IS WORKING')


def load_config():
    with open('config.toml', 'rb') as f:
        return tomllib.load(f)


def create_poster_client(config):
    return Mastodon(
        api_base_url=config['api_base_url'],
        access_token=config['poster-creds']['access_token'],
    )


if __name__ == '__main__':
    config = load_config()
    main(config)
