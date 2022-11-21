
function deleteAllCookies() {
  var cookies = document.cookie.split("; ");
  for (var c = 0; c < cookies.length; c++) {
      var d = window.location.hostname.split(".");
      while (d.length > 0) {
          var cookieBase = encodeURIComponent(cookies[c].split(";")[0].split("=")[0]) + '=; expires=Thu, 01-Jan-1970 00:00:01 GMT; domain=' + d.join('.') + ' ;path=';
          var p = location.pathname.split('/');
          document.cookie = cookieBase + '/';
          while (p.length > 0) {
              document.cookie = cookieBase + p.join('/');
              p.pop();
          };
          d.shift();
      }
  }
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp("(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

if (document.cookie.length == 0) {
  document.cookie='id_user=0'
}

if (location.href.match(/[\d\w-]+\.\w+$/)=='userlist.HTML'){
  if (getCookie('id_user')!='0') for (let i=0; i<document.getElementsByTagName('main')[0].childElementCount; i++){
    document.getElementsByClassName('newPost')[0].style.display='none'
    document.getElementsByTagName('main')[0].children[i].lastElementChild.style.display='none'
  }
  else
    for (let i=0; i<document.getElementsByTagName('main')[0].childElementCount; i++) document.getElementsByTagName('main')[0].children[i].lastElementChild.removeAttribute('style')
}

function dis_like(el){
  if (el.style.backgroundColor == 'rgb(186, 198, 210)'){
    if (el.classList.contains('dislike')) el.style.backgroundColor = '#d0a09f'
    else el.style.backgroundColor = '#96bf93'
  }
  else el.style.backgroundColor = '#bac6d2'
  
  let buttons = el.parentElement.parentElement
  let likes = buttons.getElementsByTagName
  console.log(buttons)
  fetch('/like', {
    method: 'POST',
    body: new URLSearchParams({
        'like': 24,
        'dislike': 1,
        'id': 4	
    })
});
}
