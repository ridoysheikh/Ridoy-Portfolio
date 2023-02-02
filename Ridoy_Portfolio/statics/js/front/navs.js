function tooglenavs() {
    if(document.querySelector(".main_nav").style.left == "-300px"){
        document.querySelector(".main_nav").style.left = "0px";
        document.querySelector(".togle_btn").style.left = "300px";
        document.querySelector(".material-symbols-outlined").style.transform = "rotateY(180deg)";

    } else{
        document.querySelector(".main_nav").style.left = "-300px";
        document.querySelector(".togle_btn").style.left = "0px";
        document.querySelector(".material-symbols-outlined").style.transform = "rotateY(0deg)";

    };
    
};
setInterval(() => {
    if (document.readyState ==="complete") {
        document.querySelector(".loader").style.display = "none";
    } else {
        document.querySelector(".loader").style.display = "flex";
    }
}, 10);


async function typeWriter(output,timing,rtiming,element){
    for(var i = 0; i < element.length;i++){
        document.querySelector(output).innerHTML ="";
        for(let q=0; q < element[i].length;q++){
            await new Promise(r => setTimeout(r, timing));
            document.querySelector(output).innerHTML +=element[i][q];
        }
        await new Promise(r => setTimeout(r, rtiming));
        for(let o=element[i].length; o >= 0;o--){
            await new Promise(r => setTimeout(r, timing/3));
            document.querySelector(output).innerHTML =element[i].slice(0,o);

        }
        if(i == (element.length-1)){
            i=-1;
        }
 }
}
