# -*- coding: utf-8 -*-
import argparse
import networkx as nx

parser = argparse.ArgumentParser(description='Interactive view of network')
parser.add_argument('--pickle', type=argparse.FileType('r'), required=True )
parser.add_argument('--edgelist', type=argparse.FileType('w'), required=True )
args   = parser.parse_args()

h = nx.read_gpickle( args.pickle )

for e in h.edges():
    args.edgelist.write( "%s\t%s\t%s\n".encode('utf-8') % (e[0].encode('utf-8'),
                                                         e[1].encode('utf-8'),
                                                         ",".join(h.get_edge_data(*e)['bow']).encode('utf-8')))
