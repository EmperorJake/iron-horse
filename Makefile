# Various needed programs
HG= hg
PYTHON3 = python3
SED = sed
ZIP = zip

NMLC = nmlc
GRFID = grfid

HG_INFO = bin/hg-info
FILL_TEMPLATE = bin/fill-template
FIND_FILES = bin/find-files
MK_ARCHIVE = bin/mk-archive


# Project details
PROJECT_NAME = iron-horse
SOURCES=$(shell $(FIND_FILES) --ext=.py src)

GRAPHICS_DIR = generated/graphics
LANG_DIR = generated/lang
NML_FILE = generated/iron-horse.nml
NML_FLAGS =-c -l $(LANG_DIR)

EXPORTED = no
ifeq ($(strip $(EXPORTED)),no)
  # Not exported source, therefore regular checkout
  REPO_INFO = $(shell $(HG_INFO) --num-id --version)
  REPO_REVISION = $(word 1,$(REPO_INFO))
  REPO_VERSION = $(word 2,$(REPO_INFO))
else
  # Exported version, lines below should get modified in 'bundle_src' target
  REPO_REVISION = ${exported_revision}
  REPO_VERSION = ${exported_version}
endif

REPO_TITLE = "$(PROJECT_NAME) $(REPO_VERSION)"
PROJECT_VERSIONED_NAME = $(PROJECT_NAME)-$(REPO_VERSION)
ARGS = '$(REPO_TITLE)' '$(REPO_REVISION)' '$(PW)' '$(ROSTER)'

GRF_FILE = $(PROJECT_NAME).grf
TAR_FILE = $(PROJECT_NAME).tar
ZIP_FILE = $(PROJECT_NAME).zip
MD5_FILE = $(PROJECT_NAME).check.md5

DOC_FILES = docs/license.txt docs/changelog.txt
HTML_DOCS = docs

SOURCE_NAME = $(PROJECT_VERSIONED_NAME)-source
BUNDLE_DIR = bundle_dir

# Build rules
.PHONY: default graphics lang nml grf tar bundle_tar bundle_zip bundle_src clean
default: html_docs grf
bundle_tar: tar
bundle_zip: $(ZIP_FILE)
graphics: $(GRAPHICS_DIR)
lang: $(LANG_DIR)
nml: $(NML_FILE)
grf: $(GRF_FILE)
tar: $(TAR_FILE)
html_docs: $(HTML_DOCS)

 # default num. pool workers for python compile,
 # default is 0 to disable multiprocessing (also avoids multiprocessing pickle failures masking genuine python errors)
PW = 0
ROSTER = *

# determining deps reliably for graphics generation is hard, as graphics processor depends on many things so always rebuild all
$(GRAPHICS_DIR):
	$(PYTHON3) src/render_graphics.py $(ARGS)

$(LANG_DIR):
	$(PYTHON3) src/render_lang.py $(ARGS)

$(HTML_DOCS):
	$(PYTHON3) src/render_docs.py $(ARGS)

$(NML_FILE): $(SOURCES)
	$(PYTHON3) src/render_nml.py '$(REPO_TITLE)' '$(REPO_REVISION)' '$(PW)' '$(ROSTER)'

$(GRF_FILE): $(GRAPHICS_DIR) $(LANG_DIR) $(NML_FILE)
	$(NMLC) $(NML_FLAGS) --grf=$(GRF_FILE) $(NML_FILE)

$(TAR_FILE): $(GRF_FILE) $(DOC_FILES)
	$(MK_ARCHIVE) --tar --output=$(TAR_FILE) --flatten --base=$(PROJECT_VERSIONED_NAME) $(DOC_FILES) $(GRF_FILE)

$(ZIP_FILE): $(TAR_FILE)
	$(ZIP) -9rq $(ZIP_FILE) $(TAR_FILE) >/dev/null

$(MD5_FILE): $(GRF_FILE)
	$(GRFID) -m $(GRF_FILE) > $(MD5_FILE)

bundle_src: $(MD5_FILE)
	if test -d $(BUNDLE_DIR); then rm -r $(BUNDLE_DIR); fi
	mkdir $(BUNDLE_DIR)
	$(HG) archive -t files $(BUNDLE_DIR)/src
	$(FILL_TEMPLATE) --template=Makefile \
		--output=$(BUNDLE_DIR)/src/Makefile \
		"exported_revision=$(REPO_REVISION)" \
		"exported_version=$(REPO_VERSION)"
	$(SED) -i -e 's/^EXPORTED = no/EXPORTED = yes/' $(BUNDLE_DIR)/src/Makefile
	$(MK_ARCHIVE) --tar --output=$(SOURCE_NAME).tar --base=$(SOURCE_NAME) \
		`$(FIND_FILES) $(BUNDLE_DIR)/src` $(MD5_FILE)

clean:
	for f in .chameleon_cache .nmlcache src/__pycache__ src/*/__pycache__ docs generated \
	$(GRF_FILE) $(TAR_FILE) $(ZIP_FILE) $(MD5_FILE) $(BUNDLE_DIR) $(SOURCE_NAME).tar;\
	do if test -e $$f;\
	   then rm -r $$f;\
	   fi;\
	done
