// the buttonText string says what will be written on the 
// sage cell evaluation button.
// It can be changed here.
var buttonText = "Keyra"

    
sagecell.makeSagecell({inputLocation: ".sage", evalButtonText:buttonText});
    
sagecell.makeSagecell({inputLocation: ".rsage", languages:["r"], evalButtonText: buttonText });

sagecell.makeSagecell({inputLocation: ".osage", languages:["octave"], evalButtonText: buttonText});

sagecell.makeSagecell({inputLocation: ".psage", languages:["python"], evalButtonText: buttonText});

sagecell.makeSagecell({inputLocation: ".sageAuto", evalButtonText:buttonText, autoeval: true});
    
sagecell.makeSagecell({inputLocation: ".rsageAuto", languages:["r"], evalButtonText: buttonText, autoeval: true});

sagecell.makeSagecell({inputLocation: ".osageAuto", languages:["octave"], evalButtonText: buttonText, autoeval: true});

sagecell.makeSagecell({inputLocation: ".psageAuto", languages:["python"], evalButtonText: buttonText, autoeval: true});
	
sagecell.makeSagecell({inputLocation: ".sageAutoHidden", evalButtonText :buttonText, autoeval: true, hide: ["evalButton"], template: sagecell.templates.minimal});
    
sagecell.makeSagecell({inputLocation: ".rsageAutoHidden", languages:["r"], evalButtonText: buttonText, autoeval: true, hide: ["evalButton"], template: sagecell.templates.minimal});

sagecell.makeSagecell({inputLocation: ".osageAutoHidden", languages:["octave"], evalButtonText:buttonText, autoeval: true, hide: ["evalButton"], template: sagecell.templates.minimal});

sagecell.makeSagecell({inputLocation: ".psageAutoHidden", languages:["python"], evalButtonText:buttonText, autoeval: true, hide: ["evalButton"], template: sagecell.templates.minimal});