from enum import Enum


class AllureFeature(str, Enum):
    USERS = "Users"
    GAMES = "Games"
    SETUP = "Setup"
    WISHLISTS = "Wishlists"
