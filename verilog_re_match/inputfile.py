#!/usr/bin/python3

import argparse

arg_parser = argparse.ArgumentParser( description = "Copy source_file as target_file." )
arg_parser.add_argument( "source_file" )
arg_parser.add_argument( "target_file" )
arguments = arg_parser.parse_args()

source = arguments.source_file
target = arguments.target_file
print( "Copying [{}] to [{}]".format(source, target) )