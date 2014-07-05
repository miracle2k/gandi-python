import click
import xmlrpclib


class GandiAPI(object):

    def __init__(self, api_key, api_url=None):
        self.xmlrpc = xmlrpclib.ServerProxy(
            api_url or 'https://rpc.gandi.net/xmlrpc/')
        self.key = api_key

    def dns_add(self, domain, type, name, value, ttl=None):
        # Get ID of the zone
        domain = self.xmlrpc.domain.info(self.key, domain)
        zone_id = domain['zone_id']

        # Copy the current version of the zone to a new one
        # Gandi does not allow us to modify the current zone.
        new_version_id = self.xmlrpc.domain.zone.version.new(self.key, zone_id)

        # Add the desired record
        record = {'type': type, 'name': name, 'value': value}
        if ttl:
            record['ttl'] = ttl
        self.xmlrpc.domain.zone.record.add(
            self.key, zone_id, new_version_id, record)

        # Activate the new version
        assert self.xmlrpc.domain.zone.version.set(
            self.key, zone_id, new_version_id)
        return new_version_id

    def dns_list(self, domain):
        # Get ID of the zone
        domain = self.xmlrpc.domain.info(self.key, domain)
        zone_id = domain['zone_id']

        return self.xmlrpc.domain.zone.record.list(self.key, zone_id, 0, {})


@click.group()
@click.option('--key', help='Gandi API Key')
@click.pass_context
def cli(ctx, key):
    ctx.obj = GandiAPI(key)


@cli.group()
@click.argument('domain')
@click.pass_context
def dns(ctx, domain):
    ctx.obj = (ctx.obj, domain)


@dns.command('add')
@click.argument('type')
@click.argument('name')
@click.argument('value')
@click.option('ttl')
@click.pass_obj
def dns_add((api, domain), type, name, value, ttl=None):
    api.dns_add(domain, type, name, value, ttl=ttl)


@dns.command('list')
@click.pass_obj
def dns_list((api, domain)):
    for record in api.dns_list(domain):
        print record


if __name__ == '__main__':
    cli()
