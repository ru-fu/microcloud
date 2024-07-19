import os
from git import Repo

with open(".sphinx/_integration/add_config.py", "r") as file:
    append_config = file.read()


if not os.path.isdir('.sphinx/deps/microceph'):
    Repo.clone_from('https://github.com/canonical/microceph', '.sphinx/deps/microceph', depth=1, single_branch=True, b='main')
if not os.path.islink('microceph-docs'):
    os.symlink('.sphinx/deps/microceph/docs', 'microceph-docs')
    os.remove('microceph-docs/.sphinx/_templates/header.html')
    os.symlink('../../../../../_integration/microceph.html', 'microceph-docs/.sphinx/_templates/header.html')
    os.remove('microceph-docs/.sphinx/_static/header.css')
    os.symlink('../../../../../_static/header.css', 'microceph-docs/.sphinx/_static/header.css')

    with open("microceph-docs/custom_conf.py", "a") as file:
        file.write(append_config)

if not os.path.isdir('.sphinx/deps/microovn'):
    Repo.clone_from('https://github.com/canonical/microovn', '.sphinx/deps/microovn', depth=1, single_branch=True, b='main')
if not os.path.islink('microovn-docs'):
    os.symlink('.sphinx/deps/microovn/docs', 'microovn-docs')
    os.remove('microovn-docs/.sphinx/_templates/header.html')
    os.symlink('../../../../../_integration/microovn.html', 'microovn-docs/.sphinx/_templates/header.html')
    os.remove('microovn-docs/.sphinx/_static/header.css')
    os.symlink('../../../../../_static/header.css', 'microovn-docs/.sphinx/_static/header.css')

    with open("microovn-docs/custom_conf.py", "a") as file:
        file.write(append_config)

if not os.path.isdir('.sphinx/deps/lxd'):
    Repo.clone_from('https://github.com/canonical/lxd', '.sphinx/deps/lxd', depth=1, single_branch=True, b='main')
if not os.path.isdir('lxd-docs'):
    os.mkdir('lxd-docs')
    os.symlink('../.sphinx/deps/lxd/doc', 'lxd-docs/doc')
    os.symlink('../.sphinx/deps/lxd/README.md', 'lxd-docs/README.md')
    os.symlink('../.sphinx/deps/lxd/CONTRIBUTING.md', 'lxd-docs/CONTRIBUTING.md')
    os.symlink('../.sphinx/deps/lxd/SECURITY.md', 'lxd-docs/SECURITY.md')
    os.remove('lxd-docs/doc/.sphinx/_templates/header.html')
    os.symlink('../../../../../_integration/lxd.html', 'lxd-docs/doc/.sphinx/_templates/header.html')
    os.remove('lxd-docs/doc/.sphinx/_static/header.css')
    os.symlink('../../../../../_static/header.css', 'lxd-docs/doc/.sphinx/_static/header.css')

    with open("lxd-docs/doc/custom_conf.py", "a") as file:
        file.write(append_config)
