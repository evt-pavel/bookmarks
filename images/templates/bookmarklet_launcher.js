
(function(){
    if(window.myBookmarklet!==undefined){
        myBookmarklet();
    }
    else{
        document.body.appendChild(document.createElement('script')).src='https://36f7-151-249-162-210.ngrok-free.app/static/js/bookmarklet.js?r=' + Math.floor(Math.random()*99999999999999999999);
    }
})();



