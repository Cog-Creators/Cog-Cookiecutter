# Cookiecutter template for Red cogs

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for making a cog for Red.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.5.0 or higher):

```
pip install -U cookiecutter
```

Generate a cog for Red:

```
cookiecutter https://github.com/Cog-Creators/cog-cookiecutter
```

### Supported variables

The values of variables `short`, `long`, and `install_msg` are put directly inside JSON string quotes, no escaping is done to the input.

- `package_name` - Name of a cog package. This is the folder name the cog will reside in and the name that will have to be used when loading the cog. This name should be lowercase.
- `cog_class_name` - Name of the cog's class. This name is shown in help and needs to be valid Python identifier. This name should be TitleCase.
- `config_identifier` - Config identifier for the cog. This is a unique identifier that will be used in Red's `Config`. We recommend using your Discord user ID.
- `short` - A short description of the cog. See [info.json format documentation](https://docs.discord.red/en/stable/guide_publish_cogs.html#info-json-format).
- `long` - A long description of the cog. See [info.json format documentation](https://docs.discord.red/en/stable/guide_publish_cogs.html#info-json-format).
- `install_msg` (optional) - The message that gets displayed when a cog is installed. See [info.json format documentation](https://docs.discord.red/en/stable/guide_publish_cogs.html#info-json-format).
- `authors` - Colon-separated list of authors, e.g. "Guido van Rossum; Victor Stinner; Brett Cannon". See [info.json format documentation](https://docs.discord.red/en/stable/guide_publish_cogs.html#info-json-format).
- `tags` - Space-separated list of tags, e.g. "image tools statistics". See [info.json format documentation](https://docs.discord.red/en/stable/guide_publish_cogs.html#info-json-format).
