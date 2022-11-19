
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

user_id.innerHTML='id пользователя: ' + getCookie('id_user')

function divval(event){
  ///setTimeout(location.reload(),8000)



//  let pass = prompt('Введите пароль:')
//  for (let i=0; i<document.getElementsByTagName('main')[0].childElementCount; i++) document.getElementsByTagName('main')[0].children[i].removeAttribute('style')
//  deleteAllCookies()
///  document.cookie='id_user='+ encodeURIComponent(event.firstElementChild.innerHTML)
//  user = event.firstElementChild.innerHTML
//  if (user != '0'){
//    document.getElementsByClassName('newPost')[0].style.display='none'
//    for (let i=1; i<document.getElementsByTagName('main')[0].childElementCount; i++){
//      document.getElementsByTagName('main')[0].children[i].lastElementChild.style.display='none'
//    }
//  }
  //if (getCookie('user')!='000000' && user!='000000'){
  //  document.getElementsByClassName('newPost')[0].style.display='none'
  //  for (let i=0; i<document.getElementsByTagName('main')[0].childElementCount; i++) document.getElementsByTagName('main')[0].children[i].lastElementChild.style.display='none'
  //}
//  else{
//    document.getElementsByClassName('newPost')[0].removeAttribute('style')
//    for (let i=1; i<document.getElementsByTagName('main')[0].childElementCount; i++) document.getElementsByTagName('main')[0].children[i].lastElementChild.removeAttribute('style')
//  }
//  event.style.boxShadow = "0 0 4px 3px #bac6d2"
}

//fetch('http://numbersapi.com/24')
//.then(promiseResult => { return promiseResult.text() })
//.then(function(html) {
  //var parser = new DOMParser();
//  var doc = parser.parseFromString(html, "text/html");
  //document.body.getElementsByTagName('main').appendChild(doc.documentElement)
//})

function dis_like(event){
  if (event.style.backgroundColor == 'rgb(186, 198, 210)'){
    if (event.classList.contains('dislike')) event.style.backgroundColor = '#d0a09f'
    else event.style.backgroundColor = '#96bf93'
  }
  else event.style.backgroundColor = '#bac6d2'
}
