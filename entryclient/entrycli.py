# -*- coding: utf-8 -*-
from argh.decorators import arg
from entryclient import EntryClient
import os
import logging
from optparse import OptionParser


def enter(ng_ip, ng_port, dockerd_ip, container_id):
    """
    Enter the container of specific proc
    """
    appname = 'target'

    term_type = os.environ.get("TERM", "xterm")
    endpoint = "ws://%s:%s/enter" % (ng_ip, ng_port)
    header_data = ['dockerd_ip: %s' % dockerd_ip,
                   "container_id: %s" % container_id,
                   "term-type: %s" % term_type]
    try:
        client = EntryClient(endpoint, header=header_data)
        client.invoke_shell()
    except Exception as e:
        logging.exception(e)
        print("Server stops the connection. Ask admin for help.")

def main():
    usage = 'cli.py <ng_ip> <ng_port> <dockertd_ip> <container_id>'
    parser = OptionParser(usage=usage)
    (options,args) = parser.parse_args()
    if len(args) != 4:
        parser.error('args length shall be 4!')
    ng_ip, ng_port, dockerd_ip, container_id = args[0], args[1], args[2], args[3]
    enter(ng_ip, ng_port, dockerd_ip, container_id)

if __name__ == '__main__':
    main()

