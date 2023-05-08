setInterval(() => {
    if (document.readyState ==="complete") {
        document.querySelector(".loader").style.opacity = 0;
        setTimeout(() => {
            document.querySelector(".loader").style.display = "none";
        }, 500);
    } else {
        document.querySelector(".loader").style.display = "flex";
        document.querySelector(".loader").style.opacity = 1;
    }
}, 100);
let r = document.querySelector(':root');
let tgl_btn = document.getElementById("tgl_btn");
if (window.innerWidth > 700) {
    r.style.setProperty('--nav-width', '250px');
    tgl_btn.innerText = "close";
} else {
    r.style.setProperty('--nav-width', '0px');
    tgl_btn.innerText = "menu";
}
function toggleNav(e) {
    if (r.style.getPropertyValue('--nav-width') != "0px") {
        r.style.setProperty('--nav-width', '0px');
        tgl_btn.innerText = "menu";
    } else{
        r.style.setProperty('--nav-width', '250px');
        tgl_btn.innerText = "close";
    }
}
function showMenu(e) {
    e = e || window.event;
    var target = e.target || e.srcElement;
    if (target.classList.contains("menu")) {
        if (target.classList.contains("active")) {
            target.classList.remove("active");
        } else{
            target.classList.add("active");
        }
    } else{
        if (target.parentElement.classList.contains("menu")) {
            if (target.parentElement.classList.contains("active")) {
                target.parentElement.classList.remove("active");
            } else{
                target.parentElement.classList.add("active");
            }
        } else{
            if (target.parentElement.parentElement.classList.contains("menu")) {
                if (target.parentElement.parentElement.classList.contains("active")) {
                    target.parentElement.parentElement.classList.remove("active");
                } else{
                    target.parentElement.parentElement.classList.add("active");
                }
            }
        }
    }
}
let menu = document.querySelectorAll(".menu");
for (let i = 0; i < menu.length; i++) {

    if(menu[i].querySelector('.active_sub') !== null){
        menu[i].classList.add('active')
    }
}