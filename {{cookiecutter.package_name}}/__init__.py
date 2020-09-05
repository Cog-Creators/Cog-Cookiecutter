import json
from pathlib import Path

from redbot.core.bot import Red

from .{{cookiecutter.package_name}} import {{cookiecutter.cog_class_name}}

__red_end_user_data_statement__ = "{{ cookiecutter.end_user_data_statement }}"


async def setup(bot: Red) -> None:
    bot.add_cog({{cookiecutter.cog_class_name}}(bot))
