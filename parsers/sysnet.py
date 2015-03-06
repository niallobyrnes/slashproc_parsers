#!/usr/bin/env python

from sp_parser.basic_sp_parser import BasicSPParser
from parse_helpers import traverse_directory


class Net(BasicSPParser):

    NET = "/proc/sys/net"

    @staticmethod
    def get_vars():
        """
        """

        thevars = dict()
        _, parents, all_variables = traverse_directory(Net.NET)

        for var in all_variables:
            thevars[Net.key_format(var)] = {
                'label': var,
                'unit': '',
                'parents': parents[var]
            }

        return thevars

    @staticmethod
    def get_groups():
        """
        """
        _, parents, all_variables = traverse_directory(Net.NET)

        # no need to take into account variables
        for var in all_variables:
            del parents[var]

        groups = {'sysnet': {'label': 'Network system variables', 'parents': ['root']}}

        for i in parents.keys():
            groups[Net.key_format(i)] = {
                'label': i,
                'desc': '',
                'parents': parents[i]
            }

        return groups

    @staticmethod
    def get_data(verbose=False):
        """Parse /proc/sys/net directory and its subdirs.

        Each non-directory file name is treated as variable name. Accordingly,
        file's content is treated as variable value. All groups in result
        dictionary preserve parent-child relations.

        Returns:
            tree (dict): nested dictionaries with system variables
        """

        tree, _, _ = traverse_directory(Net.NET, verbose=verbose)
        return tree


if __name__ == "__main__":
    n = Net()
    n.test_parse()