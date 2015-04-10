/**
 * Derivative of cbpAnimatedHeader.js on http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 */
var animatedHeader = (function() {

  var header = $('.navbar-fixed-top'),
  didScroll = false,
  changeHeaderOn = 300;

  function init() {
    window.addEventListener( 'scroll', function( event ) {
      if( !didScroll ) {
        didScroll = true;
        setTimeout( scrollPage, 250 );
      }
    }, false );
  }

  function scrollPage() {
    var sy = scrollY();
    if (sy >= changeHeaderOn) {
      header.addClass('navbar-shrink');
    } else {
      header.removeClass('navbar-shrink');
    }
    didScroll = false;
  }

  function scrollY() {
    return window.pageYOffset || header.scrollTop();
  }

  init();

})();


