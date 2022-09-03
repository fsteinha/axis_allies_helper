let body = document.querySelector('body');
let hamburger_icon = document.getElementById('hamburger-icon');
let menu_toggle = document.getElementById('menu-toggle');

//
// Toggle flyout on click of menu button or hamburger icon
//
hamburger_icon.addEventListener('click', toggleFlyout);
menu_toggle.addEventListener('click', toggleFlyout);

//
// Show the menu button if it is focused
//
menu_toggle.addEventListener(
  'focus',
  function() {
    menu_toggle.classList.remove('visually-hidden');  
  }
);  

//
// Hide the menu button if it is unfocused
//
menu_toggle.addEventListener(
  'blur',
  function() {
    menu_toggle.classList.add('visually-hidden');  
  }
);  

//
// Toggle flyout if enter pressed on menu button
//
menu_toggle.addEventListener(
  'keyup', 
  function(e) {    
    if ( e.keyCode == 13) {
      e.preventDefault();  
      showFlyout();
      return false;
    }
  }
);

//
// Hide flyout if escape pressed while it is open
//
body.addEventListener(
  'keyup', 
  function(e) {
    if ( e.keyCode == 27 && body.classList.contains('flyout-open') ) {
      e.preventDefault();
      hideFlyout();
      return false;
    }
  }
);

function showFlyout() {
  
  let menu_toggle = document.getElementById('menu-toggle');
  let flyout = document.getElementById('flyout-menu');
  
  body.classList.add('flyout-open');
  menu_toggle.setAttribute('aria-expanded', true);
  flyout.setAttribute('aria-hidden', false);
  
}

function hideFlyout() {
  
  let menu_toggle = document.getElementById('menu-toggle');
  let flyout = document.getElementById('flyout-menu');
  
  body.classList.remove('flyout-open');
  menu_toggle.setAttribute('aria-expanded', false);
  flyout.setAttribute('aria-hidden', true);
  
}

function toggleFlyout() {
  
  let body = document.querySelector('body');
  let menu_toggle = document.getElementById('menu-toggle');
  let flyout = document.getElementById('flyout-menu');
  
  if ( body.classList.contains('flyout-open') ) {
    hideFlyout();
  }
  else {
    showFlyout();
  }  
}
