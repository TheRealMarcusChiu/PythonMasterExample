import sys
import os
import subprocess
import re
from os import listdir
from os.path import isfile, join
import urllib


BASE_DIR = os.getcwd()
SVN_BASE    = "https://ps-svn.aws.marketlive.com/marketlive/"
SITES       = "sites/"
MARKETLIVE_HOME = os.environ["MARKETLIVE_HOME"]
TOMCAT_SCRIPTS  = MARKETLIVE_HOME + "/tomcat/apache-tomcat-7.0.52/bin/"
TOMCAT_DIR = "/tomcat/apache-tomcat-7.0.52/bin/"
S3_URL = "https://s3-us-west-1.amazonaws.com/kibo-files/"

commands = ["options", "buildsite", "deploysite", "getsite", "setupdb", "setuptomcat", "refreshmongo", "snapshot",
            "tomcatstop", "tomcatstart", "tomcatrestart", "tail", "getdependencies", "quickbuild", "updatems"]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def update_ms_servers_overrides(site="jesus", version="1.0v", branch=None):
    print "inside the update"

if __name__=="__main__":
    update_ms_servers_overrides()
    
    num_args = len(sys.argv)

    # At least one argument is required
    if num_args < 2:
        print
        print "usage: python manage.py <command> <options>"
        print bcolors.BOLD + bcolors.FAIL + "error: Must provide a valid argument" + bcolors.ENDC
        print
        sys.exit(1)

    # Invalid command
    if num_args >= 2:
        print "inside"
        print sys.argv[1]

    command = "pwd"
    subprocess.call(command, shell=True)

    f = open(MARKETLIVE_HOME + "/sites/" + "countrycurtains" + "/trunk/source/ant/sites.xml", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        try:
            if not "<section " in line:
                continue

            paths = re.findall(r'\"(.+?)"', line)

            _type = paths[0]

            print "found: " + _type

        except ValueError:
            pass

    print "finished"
