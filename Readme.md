##Install

    pip install j2g

##How to use

    python -m j2g -h
    usage: j2g [-h] [-v] [-f {pdf,jpg,png}] [-n ROOT_NODE_NAME] [-p] [-q] source destination
    
    This is a json graph util j2g version=0.0.1. jeack_chen@hotmail.com
    
    positional arguments:
      source                json file
      destination           Prefix the output file.
    
    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -f {pdf,jpg,png}, --format {pdf,jpg,png}
                            Type of the output file
      -n ROOT_NODE_NAME, --root_node_name ROOT_NODE_NAME
                            root node name
      -p, --power           If the output file exists, overwrite it.
      -q, --quiet           Quiet work, do not display a completion message.

##More

    https://github.com/jeackchn/j2g
