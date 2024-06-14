import os
from git import Repo

if not os.path.isdir('.sphinx/deps/microceph'):
    Repo.clone_from('https://github.com/canonical/microceph', '.sphinx/deps/microceph', depth=1, single_branch=True, b='main')
if not os.path.islink('microceph-docs'):
    os.symlink('.sphinx/deps/microceph/docs', 'microceph-docs')

if not os.path.isdir('.sphinx/deps/microovn'):
    Repo.clone_from('https://github.com/canonical/microovn', '.sphinx/deps/microovn', depth=1, single_branch=True, b='main')
if not os.path.islink('microovn-docs'):
    os.symlink('.sphinx/deps/microovn/docs', 'microovn-docs')

if not os.path.isdir('.sphinx/deps/lxd'):
    Repo.clone_from('https://github.com/canonical/lxd', '.sphinx/deps/lxd', depth=1, single_branch=True, b='main')
if not os.path.islink('lxd-docs'):
    os.symlink('.sphinx/deps/lxd/doc', 'lxd-docs')
