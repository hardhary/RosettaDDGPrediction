#!/usr/bin/env python
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-

#    defaults.py
#
#    Hard-coded default parameters. Should only be changed
#    for development purposes.
#
#    Copyright (C) 2020 Valentina Sora 
#                       <sora.valentina1@gmail.com>
#                       Matteo Tiberti 
#                       <matteo.tiberti@gmail.com> 
#                       Elena Papaleo
#                       <elenap@cancer.dk>
#
#    This program is free software: you can redistribute it and/or
#    modify it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public
#    License along with this program. 
#    If not, see <http://www.gnu.org/licenses/>.


import collections
import os.path
from pkg_resources import resource_filename, Requirement



############################ STEPS/OPTIONS ############################



# recognized protocols
ROSETTAPROTOCOLS = \
    {"flexddg" : \
        {"flexddg" : {"role" : "ddg", \
                      "runby" : "rosetta", \
                      "executable" : "rosetta_scripts"}}, \
    "cartddg" : \
        {"relax" : {"role" : "processing", \
                    "runby" : "rosetta", \
                    "executable" : "relax"}, \
         "structure_selection" : {"runby" : "python"}, \
         "cartesian" : {"role" : "ddg", \
                        "runby" : "rosetta", \
                        "executable" : "cartesian_ddg"}}, \
    }


# possible ways of defining various Rosetta options that
# are needed to correctly retrieve files/parameters
ROSETTAOPTIONS = \
    collections.defaultdict(str,\
        {"ddgout" : ("-ddg:out", "-out"), \
         "inpdbfile" : ("-in:file:s", "-s"), \
         "mutfile" : ("-ddg:mut_file", "-mut_file"), \
         "outprefix" : ("-out:prefix", "-prefix"), \
         "outsuffix" : ("-out:suffix", "-suffix"), \
         "scriptvars" : ("-parser:script_vars", "-script_vars"), \
         "scorefile" : ("-out:file:scorefile", "-scorefile"), \
         "scfname" : ("-score:weights", "-weights", "scfname"), \
         "backrubntrials" : ("backrubntrials",), \
         "backrubtrajstride" : ("backrubtrajstride",), \
         "ddgdbfile" : ("ddgdbfile",), \
         "protocol" : ("-parser:protocol", "-protocol"), \
         "resfile" : ("resfile",), \
         "structdbfile" : ("structdbfile",)})



########################## DIRECTORIES/FILES ##########################



# directory containing configuration files for running the protocols
CONFIGRUNDIR = \
    resource_filename(Requirement("RosettaDDGProtocols"), \
                      "RosettaDDGProtocols/config_run")

# directory containing configuration files for aggregating results
CONFIGAGGRDIR = \
    resource_filename(Requirement("RosettaDDGProtocols"), \
                      "RosettaDDGProtocols/config_aggregate")

# directory containing configuration files for plotting
CONFIGPLOTDIR = \
    resource_filename(Requirement("RosettaDDGProtocols"), \
                      "RosettaDDGProtocols/config_plot")

# directory containing configuration files for run settings
CONFIGSETTINGSDIR = \
    resource_filename(Requirement("RosettaDDGProtocols"), \
                      "RosettaDDGProtocols/config_settings")

# directory containing RosettaScripts used in some protocols
ROSETTASCRIPTSDIR = \
    resource_filename(Requirement("RosettaDDGProtocols"), \
                    "RosettaDDGProtocols/RosettaScripts")

# default configuration file for data aggregation
CONFIGAGGRFILE = os.path.join(CONFIGAGGRDIR, "aggregate.yaml")

# default configuration file for run settings
CONFIGSETTINGSFILE = os.path.join(CONFIGSETTINGSDIR, "nompi.yaml")



############################## MUTATIONS ##############################



### keywords used to refer to specific mutation attributes

# mutation (maps to as many dictionaries as the single mutations
# defined)
MUT = "_mut_"

# structure number/ID (in case the same mutation must be performed
# multiple times on the same structure to obtain an ensemble)
STRUCT = "_struct_"

# wild-type residue in a single mutation
WTR = "_wtr_"

# mutant residue in a single mutation
MUTR = "_mutr_"

# residue number in a single mutation
NUMR = "_numr_"

# chain ID in a single mutation
CHAIN = "_chain_"

# all attributes that are not the mutant residue
NOMUTR = "_nomutr_"

# mutation directory path
MUTDIRPATH = "_dirpath_"

# mutation directory name
MUTDIRNAME = "_dirname_"

# separator for mutations that are performed simultaneously    
MUTSEP = ","

# separator for the components of a mutation
# (e.g. C.L.53 for mutating L53 on chain C)
COMPSEP = "."

DIRCHAINSEP = "-"

DIRMUTSEP = "_"



############################# AGGREGATION #############################



# column names in Rosetta .db3 files and aggregated dataframes
ROSETTADFCOLS = {"scfname" : "score_function_name", \
                 "bsteps" : "backrub_steps", \
                 "energyunit" : "energy_unit", \
                 "mutation" : "mutation", \
                 "name" : "name", \
                 "nstruct" : "nstruct", \
                 "sctype" : "score_type_name", \
                 "scvalue" : "score_value", \
                 "state" : "state", \
                 "structid" : "struct_id", \
                 "structnum" : "struct_num", \
                 "totscore" : "total_score"}


############################### PLOTTING ##############################



PLOTTYPES = ["total_heatmap", "total_heatmap_saturation", \
             "contributions_barplot", "dg_swarmplot"]