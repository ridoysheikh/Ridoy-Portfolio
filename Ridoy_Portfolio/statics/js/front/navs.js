function tooglenavs() {
    if(document.querySelector(".main_nav").style.left == "-300px"){
        document.querySelector(".main_nav").style.left = "0px";
        document.querySelector(".togle_btn").style.left = "300px";
        document.querySelector(".material-symbols-outlined").style.transform = "rotateY(180deg)";

    } else{
        document.querySelector(".main_nav").style.left = "-300px";
        document.querySelector(".togle_btn").style.left = "0px";
        document.querySelector(".material-symbols-outlined").style.transform = "rotateY(0deg)";

    }
    
}