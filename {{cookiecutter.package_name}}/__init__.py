from redbot.core.bot import Red

from .{{cookiecutter.package_name}} import {{cookiecutter.cog_class_name}}


async def setup(bot: Red) -> None:
    bot.add_cog({{cookiecutter.cog_class_name}}(bot))
