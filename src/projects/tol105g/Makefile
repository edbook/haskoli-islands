PROJECT=$(notdir $(CURDIR))
PROJECTCSS=_static/css/$(PROJECT).css
BUILD=../../../_build/$(PROJECT)
BUILDCSS=$(BUILD)/_static/css/$(PROJECT).css
BDIR=$(CURDIR)/html

build:	$(BUILDCSS)
	$(MAKE) --directory=../../.. build project=$(PROJECT)

css:
	@$(MAKE) $(BUILDCSS)

auto:	$(BUILDCSS)
	@echo AFTER BUILDING, NAVIGATE TO localhost:8000 in browser
	@echo
	$(MAKE) --directory=../../.. autobuild project=$(PROJECT)

www:
	$(MAKE) build
	copy-to-cs $(BUILD) /Volumes/cs/t1a

$(BUILDCSS): $(PROJECTCSS)
	cp $(PROJECTCSS) $(BUILDCSS)
