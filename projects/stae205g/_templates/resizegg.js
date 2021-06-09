// Fengid ad lani hedan: https://css-tricks.com/NetMag/FluidWidthVideo/Article-FluidWidthVideo.php
// med sma breytingum

$(function() {
    // Find all geogebra applets
    var $allGA= $("iframe[src^='https://tube.geogebra.org']"),

    // The element that is fluid width
    $fluidEl = $("figure");

    // Figure out and save aspect ratio for each applet
    $allGA.each(function() {

      $(this)
        .data('aspectRatio', this.height / this.width)

        // and remove the hard coded width/height
        .removeAttr('height')
        .removeAttr('width');

    });

    // When the window is resized
    $(window).resize(function() {

      var newWidth = $fluidEl.width();

      // Resize all applets according to their own aspect ratio
      $allGA.each(function() {

        var $el = $(this);
        $el
          .width(newWidth)
          .height(newWidth * $el.data('aspectRatio'))
          .attr('src',$el.attr('src'));

      });

    // Kick off one resize to fix all videos on page load
    }).resize();
});