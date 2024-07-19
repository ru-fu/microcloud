import os
import wget
import argparse

parser = argparse.ArgumentParser(description='Update the subprojects to work as part of the MicroCloud documentation.')

parser.add_argument('--project', '-p', required=True, choices = ['lxd', 'microceph', 'microovn'], help='The subproject to integrate')
parser.add_argument('--download-from', '-d', nargs='?', default='remote', choices = ['remote', 'local'], help='From where to download the integration files')

args = vars(parser.parse_args())
print(args)

if args['download_from'] == "remote":
    config_file = wget.download("https://raw.githubusercontent.com/ru-fu/microcloud/LXD-1097-build-separately-subprojects/doc/.sphinx/_integration/add_config.py")
    header = wget.download("https://raw.githubusercontent.com/ru-fu/microcloud/LXD-1097-build-separately-subprojects/doc/.sphinx/_integration/" + args['project'] + ".html")
    headercss = wget.download("https://raw.githubusercontent.com/ru-fu/microcloud/LXD-1097-build-separately-subprojects/doc/.sphinx/_static/header.css")
    prefix = ""
else:
    config_file = ".sphinx/_integration/add_config.py"
    header = ".sphinx/_integration/" + args['project'] + ".html"
    headercss = ".sphinx/_static/header.css"
    if args['project'] == "lxd":
        prefix = args['project'] + "/doc/"
    else:
        prefix = args['project'] + "/docs/"

with open(config_file, "r") as file:
    append_config = file.read()


os.remove(prefix + '.sphinx/_templates/header.html')
os.popen('cp '+ header + ' ' + prefix + '.sphinx/_templates/header.html')

os.remove(prefix + '.sphinx/_static/header.css')
os.popen('cp '+ headercss + ' ' + prefix + '.sphinx/_static/header.css')

with open(prefix + "custom_conf.py", "a") as file:
    file.write(append_config)
