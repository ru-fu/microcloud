import os

for root, dirs, files in os.walk('lxd-docs/'):
    if root.find(".sphinx") == -1:
        for file in files:

            if file == "manpages.md":
                with open(os.path.join(root, file), 'w') as mdfile:
                    mdfile.write("(manpages)=\n# Man pages\n\nThe man pages for the `lxc` command are available in the [LXD documentation](https://documentation.ubuntu.com/lxd/en/latest/reference/manpages/lxc/).\n")

            if file.endswith(".md") and not file == "api.md" and not file.startswith("root-"):
#                print(os.path.join(root, file))
                with open(os.path.join(root, file), 'r') as mdfile:
                    content = mdfile.readlines()
                with open(os.path.join(root, file), 'w') as mdfile:
                    for line in content:
                        if line.startswith(':diataxis:self'):
                            continue
                        if line.startswith('/') and not line.startswith('/1.0'):
                            mdfile.write('/lxd-docs' + line)
                        elif line.find('{doc}`/') > -1:
                            mdfile.write(line.replace('{doc}`/','{doc}`/lxd-docs/'))
                        elif line.find('{figure} /') > -1:
                            mdfile.write(line.replace('{figure} /','{figure} /lxd-docs/'))
                        elif line.find('{include} /') > -1:
                            mdfile.write(line.replace('{include} /','{include} /lxd-docs/'))
                        elif line.find('{include} ../README') > -1:
                            mdfile.write(line.replace('{include} ../README','{include} /lxd-docs/root-README'))
                        elif line.find('{include} ../../README') > -1:
                            mdfile.write(line.replace('{include} ../../README','{include} /lxd-docs/root-README'))
                        elif line.find('{include} ../../SECURITY') > -1:
                            mdfile.write(line.replace('{include} ../../SECURITY','{include} /lxd-docs/root-SECURITY'))
                        elif line.find('{include} ../CONTRIBUTING') > -1:
                            mdfile.write(line.replace('{include} ../CONTRIBUTING','{include} /lxd-docs/root-CONTRIBUTING'))
                        elif (line.find('</') > -1 and
                              line.find('</a>') == -1 and
                              line.find('</audio>') == -1 and
                              line.find('</code>') == -1 and
                              line.find('</details>') == -1 and
                              line.find('</summary>') == -1 ):
                            mdfile.write(line.replace('</','</lxd-docs/'))
                        elif line.find('](/') > -1:
                            mdfile.write(line.replace('](/','](/lxd-docs/'))
                        elif line.find(':diataxis:/') > -1:
                            mdfile.write(line.replace(':diataxis:/',':diataxis:/lxd-docs/'))
                        else:
                            mdfile.write(line)




for root, dirs, files in os.walk('microovn-docs/'):
    if root.find(".sphinx") == -1:
        for file in files:

            if file.endswith(".rst"):
#                print(os.path.join(root, file))
                with open(os.path.join(root, file), 'r') as mdfile:
                    content = mdfile.readlines()
                with open(os.path.join(root, file), 'w') as mdfile:
                    for line in content:
                        if (line.find('</') > -1 and
                            line.find('</a>') == -1 and
                            line.find('</audio>') == -1 and
                            line.find('</code>') == -1 and
                            line.find('</details>') == -1 and
                            line.find('</summary>') == -1 ):
                            mdfile.write(line.replace('</','</microovn-docs/'))
                        else:
                            mdfile.write(line)
