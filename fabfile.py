from fabric.api import *
import fabric.contrib.project as project


def build():
    local('lessc static/css/style.less > static/css/style.css')
    