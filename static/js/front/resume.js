function checkVisible(elm) {
    var rect = elm.getBoundingClientRect();
    var viewHeight = Math.max(document.documentElement.clientHeight, window.innerHeight);
    return !(rect.bottom < 0 || rect.top - viewHeight >= 0);
  };
setInterval(() => {
    let elmnt = document.querySelectorAll(".edu_container");
    for (let i = 0; i < elmnt.length; i++) {
        if (checkVisible(elmnt[i])) {
            elmnt[i].style.opacity = "1";
            elmnt[i].style.marginLeft = "0";
        }
    }
}, 100);