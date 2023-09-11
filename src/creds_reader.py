import configparser


def get_credentials():
    config = configparser.ConfigParser()
    config.read("credentials.ini")
    return {
        "client_id": config.get("credentials", "client_id"),
        "client_secret": config.get("credentials", "client_secret"),
    }
