PROJECT=$(notdir $(CURDIR))
PROJECTCSSDIR=_static/css/$(PROJECT).css
PROJECTCSS=$(PROJECTCSSDIR)/$(PROJECT).css
BUILD=../../../_build/$(PROJECT)
BUILDCSSDIR=$(BUILD)/_static/css/$(PROJECT).css
BUILSCSS=$(BUILDCSSDIR)/$(PROJECT).css

build:	$(BUILDCSS)
	$(MAKE) --directory=../../.. build project=$(PROJECT)

css:
	@$(MAKE) $(BUILDCSS)

auto:	$(BUILDCSS)
	@echo AFTER BUILDING, NAVIGATE TO localhost:8000 in browser
	@echo
	$(MAKE) --directory=../../.. autobuild project=$(PROJECT)

clean:
	rm -rf $(BUILD)

www:
	$(MAKE) build
	rsync -vru $(BUILD)/ pluto:/mnt/$(PROJECT)

$(BUILDCSS): $(PROJECTCSS)
	mkdir -p $(BUILDCSSDIR)
	cp $(PROJECTCSS) $(BUILDCSS)
