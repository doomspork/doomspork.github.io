document.addEventListener('DOMContentLoaded', function () {
  // Decode email address
  var meta_contact = getAll('meta[name=contact]');
  var meta_key = meta_contact[0].getAttribute('data-key');
  var meta_encoded = meta_contact[0].getAttribute('data-encoded');

  var emails = getAll(".has-secret-email");
  emails.forEach(function(element){
    element.setAttribute("href", "mailto:" + decode_email(meta_key, meta_encoded));
    element.textContent = decode_email(meta_key, meta_encoded);
  });
  var emails = getAll(".has-secret-action");
  emails.forEach(function(element){
    element.setAttribute("action", "https://formspree.io/" + decode_email(meta_key, meta_encoded));
  });
  var emails = getAll(".has-secret-mailto");
  emails.forEach(function(element){
    element.setAttribute("href", "mailto:" + decode_email(meta_key, meta_encoded));
  });

  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {
        // Get the target from the "data-target" attribute
        var target = document.getElementById($el.dataset.target);
        var hero = document.getElementById($el.dataset.hero); // change this name
        var hide = document.getElementById($el.dataset.hide); // hide the hero body
        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        document.documentElement.classList.toggle('is-disabled'); // <html>
        $el.classList.toggle('is-active'); // burger
        if (hide){
          console.log('hidden');
          hide.classList.toggle('is-hidden'); // body
        }
        target.classList.toggle('is-active'); // menu
        if (hero.classList.contains('is-sean') != true){
          hero.classList.toggle('is-fullheight');  
        }
      });
    });
  }
  
  function decode_email(key, coded) {
    shift=coded.length
    link=""
    for (i=0; i<coded.length; i++) {
      if (key.indexOf(coded.charAt(i))==-1) {
        ltr = coded.charAt(i)
        link += (ltr)
      }
      else {
        ltr = (key.indexOf(coded.charAt(i))-shift+key.length) % key.length
        link += (key.charAt(ltr))
      }
    }
    return link
  }
  
  function getAll(selector) {
    return Array.prototype.slice.call(document.querySelectorAll(selector), 0);
  }
});
