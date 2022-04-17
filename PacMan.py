import click
import commands
import os

@click.command('add', short_help='Add new entry')
def add():
    commands.add.add_c()

@click.command('config', short_help = 'config for the first time')
def config():
    commands.config.config_c()

@click.command('create', short_help='Create local PacMan database')
def create():
    commands.create.create_c()

@click.command('list', short_help='Display the entries')
def list():
    commands.display.display_c()

@click.command('help', short_help='Display Help')
@click.pass_context
def help(context):
    click.echo(context.parent.get_help())

@click.command('remove', short_help='Remove the entries from the list')
def remove():
    commands.remove.remove_C()

@click.command('update', short_help = 'update the values in the list')
def update():
    commands.update.update_c()
    
@click.command('upgrade', short_help = 'manual upgrade packages in the list')
def upgrade():
    commands.upgrade.upgrade_c()
    
@click.group(add_help_option=False)
@click.pass_context
def PacMan(context):
    """
    PacMan - personal pacman
    """

PacMan.add_command(add)
PacMan.add_command(config)
PacMan.add_command(create)
PacMan.add_command(help)
PacMan.add_command(list)
PacMan.add_command(remove)
PacMan.add_command(update)
PacMan.add_command(upgrade)

if __name__ == "__main__":
    PacMan()