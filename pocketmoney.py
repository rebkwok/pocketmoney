import click
from transactions import add_transaction, get_balance


@click.group()
def cli():
    pass


@cli.command()
@click.argument('description')
@click.argument('in_amount', type=float)
def deposit(description, in_amount):
    add_transaction(description, in_amount, '')
    click.echo('New balance: {}'.format(get_balance()))


@cli.command()
@click.argument('description')
@click.argument('out_amount', type=float)
def withdraw(description, out_amount):
    add_transaction(description, '', out_amount)
    click.echo('New balance: {}'.format(get_balance()))


@cli.command()
def balance():
    click.echo(get_balance())


if __name__ == '__main__':
    cli()
