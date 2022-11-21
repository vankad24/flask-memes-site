if (document.cookie.length == 0) {
  document.cookie='id_user=0'
}

function dis_like(el){
  count = el.parentElement.querySelector("a")
  if (el.style.backgroundColor == 'rgb(186, 198, 210)'){
    if (el.classList.contains('dis')) el.style.backgroundColor = '#d0a09f'
    else el.style.backgroundColor = '#96bf93'
	count.innerText = parseInt(count.innerText)+1
  }else {
	  el.style.backgroundColor = '#bac6d2'
	  count.innerText = parseInt(count.innerText)-1
  }
  let post = el.closest(".flex")
  let likes = post.querySelector("a[name='like']").innerText
  let dislikes = post.querySelector("a[name='dislike']").innerText
  let id = post.getAttribute("post_id")
  
  fetch('/like', {
    method: 'POST',
    body: new URLSearchParams({
        'like': likes,
        'dislike': dislikes,
        'id': id	
    })
  });
}
