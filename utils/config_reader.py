import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")


def get_base_url():
    return config.get("DEFAULT", "base_url")


def get_browser():
    return config.get("DEFAULT", "browser")


def username():
    return config.get("DEFAULT", "username")


def password():
    return config.get("DEFAULT", "password")
