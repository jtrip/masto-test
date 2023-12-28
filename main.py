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


def get_account_data(client, account_id=None):
    """Get account data from API, default to client user if no account_id given."""
    if account_id:
        account_data = client.account(account_id)
    else:
        account_data = client.me()
    return account_data


def get_account_statuses(client, account_id=None):
    """Get account statuses from API, default to client user if no account_id given."""
    if account_id:
        statuses = client.account_statuses(account_id)
    else:
        statuses = client.account_statuses(client.me()['id'])
    return statuses


def post_msg(client, msg):
    client.toot(msg)


def load_config():
    with open('config.toml', 'rb') as f:
        return tomllib.load(f)


def create_poster_client(config):
    return Mastodon(
        api_base_url=config['api_base_url'],
        access_token=config['poster-creds']['access_token'],
    )


def main(config):
    mastodon_client = create_poster_client(config)
    post_msg(mastodon_client, 'API POSTER IS WORKING')


if __name__ == '__main__':
    config = load_config()
    main(config)
