import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config


class {{ cookiecutter.cog_class_name }}(commands.Cog):
    """
    {{ cookiecutter.short }}
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier={{ cookiecutter.config_identifier }},
            force_registration=True,
        )
