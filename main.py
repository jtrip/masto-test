from mastodon import Mastodon
import tomllib


def post_msg(client, msg):
    client.toot(msg)


def main(config):
    mastodon_client = Mastodon(
        api_base_url=config['api_base_url'],
        access_token=config['poster-creds']['access_token'],
    )
    post_msg(mastodon_client, 'API POSTER IS WORKING')


if __name__ == '__main__':
    # load config
    with open('config.toml', 'rb') as f:
        config = tomllib.load(f)
    main(config)
