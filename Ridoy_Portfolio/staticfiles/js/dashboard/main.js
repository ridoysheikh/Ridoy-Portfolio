let r = document.querySelector(':root');
let tgl_btn = document.getElementById("tgl_btn");
console.log(screen.width);
if (screen.width > 700) {
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