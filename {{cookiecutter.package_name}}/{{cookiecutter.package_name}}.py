from typing import Literal

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


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

    async def red_delete_data_for_user(self, *, requester: RequesterType, user_id: int) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)
