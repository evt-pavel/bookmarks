(function(){
  if(!window.bookmarklet) {
  bookmarklet_js = document.body.appendChild(document.
  createElement('script'));
  bookmarklet_js.src = 'https://3145-151-249-166-236.ngrok-free.app/static/js/bookmarklet.js?r='+Math.
  floor(Math.random()*9999999999999999);
  window.bookmarklet = true;
  }
  else {
  bookmarkletLaunch();
  }
  })();