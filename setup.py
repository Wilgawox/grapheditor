# This Setup script has been commented to ease the writing of your own file. 

# A setup script mainly consist of a call to the setup function of setuptool, that allows to create a distribution archive of a set of python modules grouped in packages (ie in directories with an __init__.py file).
# In the context of OpenAlea, this function has been extended by the openalea.deploy module to ease the simultaneaous distribution of binaries and libraries.



# (To adapt this script for your package, you mainly have to change the content of the variable defined before the call to setup function, and comment out unused options in the call of the function)

import sys
import os

from setuptools import setup, find_packages


# Name and version of for your 'distribution archive'

# (This will determine the name of the egg, as well as the name of the pakage directory under Python/lib/site-packages)
# (This name is also the one to use in setup script of other packages to declare a dependency to this package)
# (The version number is used by deploy to detect UPDATES)

name = 'OpenAlea.GraphEditor'
version= '0.7.0' 

# Packages list, namespace and root directory of packages

# (this will determine the archive content and the names of your modules)
# (with the loop used bellow,all packages,ie all directories with a __init__.py, under pkg_root_dir will be recursively detected and named according to the directory hirearchy)
# (namespace allows you to choose a prefix for package names (eg alinea, openalea,...). 
# (This functionality needs deploy to be installed)
# (if you want more control on what to put in your distribution, you can manually edit the' packages' list 
# (the 'package_dir' dictionary must content the pkg_rootdir and all top-level pakages under it)

namespace = 'openalea'
pkg_root_dir = 'src'
pkgs = [ pkg for pkg in find_packages(pkg_root_dir) if namespace not in pkg]
top_pkgs = [pkg for pkg in pkgs if  len(pkg.split('.')) < 2]
packages = [ namespace + "." + pkg for pkg in pkgs]
package_dir = dict( [('',pkg_root_dir)] + [(namespace + "." + pkg, pkg_root_dir + "/" + pkg) for pkg in top_pkgs] )

# List of top level wralea packages (directories with __wralea__.py) 
# (to be kept only if you have visual components)
#wralea_entry_points = ['%s = %s'%(pkg,namespace + '.' + pkg) for pkg in top_pkgs]

# Meta information
# (used to construct egg infos)
description= 'GraphEditor package for OpenAlea.' 
long_description= '''
An attempt at generalising the viewing and interacting of
various sorts of graphs.
'''
author= 'Daniel Barbeau'
author_email= 'daniel.barbeau@sophia.inria.fr'
url= 'http://openalea.gforge.inria.fr'
license= 'Cecill-C' 

# dependencies to other eggs
# (This is used by deploy to automatically downloads eggs during the installation of your package)
# (allows 'one click' installation for windows user)
# (linux users generally want to void this behaviour and will use the dependance list of your documentation)
# (dependance to deploy is mandatory for runing this script)
setup_requires = ['openalea.deploy']
if("win32" in sys.platform):
    install_requires = ['openalea.core']
else:
    install_requires = ['openalea.core']
# web sites where to find eggs
dependency_links = ['http://openalea.gforge.inria.fr/pi']

# setup function call
#
setup(
    # Meta data (no edition needed if you correctly defined the variables above)
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords = '',	
    # package installation
    packages= packages,	
    package_dir= package_dir,
    # Namespace packages creation by deploy
    namespace_packages = [namespace],
    create_namespaces = True,
    # tell setup not  tocreate a zip file but install the egg as a directory (recomended to be set to False)
    zip_safe= False,
    # Dependencies
    setup_requires = setup_requires,
    install_requires = install_requires,
    dependency_links = dependency_links,


    # Eventually include data in your package
    # (flowing is to include all versioned files other than .py)
    include_package_data = True,
    # (you can provide an exclusion dictionary named exclude_package_data to remove parasites).
    # alternatively to global inclusion, list the file to include   
    #package_data = {'' : ['*.pyd', '*.so'],},

    # postinstall_scripts = ['',],

    # Declare scripts and wralea as entry_points (extensions) of your package 
    entry_points = { 
		    #'console_scripts': [
                     #       'fake_script = openalea.fakepackage.amodule:console_script', ],
                     # 'gui_scripts': [
                      #      'fake_gui = openalea.fakepackage.amodule:gui_script',],
		#	'wralea': wralea_entry_points
		},
    )


