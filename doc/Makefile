# This Makefile stub allows you to customize starter pack (SP) targets.
# Consider this file as a bridge between your project
# and the starter pack's predefined targets that reside in Makefile.sp.
#
# You can add your own, non-SP targets here or override SP targets
# to fit your project's needs. For example, you can define and use targets
# named "install" or "run", but continue to use SP targets like "sp-install"
# or "sp-run" when working on the documentation.

SPHINXDIR     = .sphinx
VENVDIR       = $(SPHINXDIR)/venv
VENV          = $(VENVDIR)/bin/activate


# Put it first so that "make" without argument is like "make help".
help:
	@echo "\n" \
        "------------------------------------------------------------- \n" \
        "* watch, build and serve the documentation:  make run \n" \
        "* only build:                                make html \n" \
        "* only serve:                                make serve \n" \
        "* clean built doc files:                     make clean-doc \n" \
        "* clean full environment:                    make clean \n" \
        "* check links:                               make linkcheck \n" \
        "* check spelling:                            make spelling \n" \
        "* check spelling (without building again):   make spellcheck \n" \
        "* check inclusive language:                  make woke \n" \
        "* check accessibility:                       make pa11y \n" \
        "* other possible targets:                    make <TAB twice> \n" \
        "------------------------------------------------------------- \n"

deps:
	mkdir -p lxd/ microceph/ microovn/
	cd lxd && git restore doc/custom_conf.py || true
	cd microceph && git restore docs/custom_conf.py || true
	cd microovn && git restore docs/custom_conf.py || true
	git -C lxd pull || git clone --depth 1 https://github.com/canonical/lxd lxd
	git -C microceph pull || git clone --depth 1 https://github.com/canonical/microceph microceph
	git -C microovn pull || git clone --depth 1 https://github.com/canonical/microovn microovn
	python3 .sphinx/_integration/integrate-docs.py --project lxd -d local
	python3 .sphinx/_integration/integrate-docs.py --project microceph -d local
	python3 .sphinx/_integration/integrate-docs.py --project microovn -d local

deps-clean:
	rm -rf lxd/ microceph/ microovn/

current_dir := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))

.PHONY: deps
deps-doc: deps
	mkdir -p _build/projects
	cd lxd && make doc
	rm -rf _build/projects/lxd
	mv lxd/doc/_build _build/projects/lxd
	cd microceph/docs && make html
	rm -rf _build/projects/microceph
	mv microceph/docs/_build _build/projects/microceph
	cd microovn/docs && make html
	rm -rf _build/projects/microovn
	mv microovn/docs/_build _build/projects/microovn
	make html

clean: deps-clean
	$(MAKE) -f Makefile.sp sp-clean

%:
	$(MAKE) -f Makefile.sp sp-$@
