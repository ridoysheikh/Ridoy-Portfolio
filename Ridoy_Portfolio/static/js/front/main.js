let txt = ["Freelauncer", "Web Devoloper", "Web Designer"]
window.onload = typeWriter(".profs",50,2000,txt);


var bgimage;
let counti = 0;
if (screen.width < 800) {
  fetch(`/api/?name=bgimage&screen=Portrait`).then(response => response.json())
  .then(data => {
    data = JSON.stringify(data);
    bgimages=JSON.parse(data).images;
    document.querySelector(".bg_container").style.backgroundImage = `url(/media/${bgimages[counti]})`;
    setInterval(() => {
      counti++
      if (counti >= bgimages.length) {
        counti = 0;
      }
      document.querySelector(".bg_container").style.backgroundImage = `url(/media/${bgimages[counti]})`;
    }, 5000);
  })
} else{
  fetch(`/api/?name=bgimage&screen=Landscape`).then(response => response.json())
  .then(data => {
    data = JSON.stringify(data);
    bgimages=JSON.parse(data).images;
    document.querySelector(".bg_container").style.backgroundImage = `url(/media/${bgimages[counti]})`;
    setInterval(() => {
      counti++
      if (counti >= bgimages.length) {
        counti = 0;
      }
      document.querySelector(".bg_container").style.backgroundImage = `url(/media/${bgimages[counti]})`;
    }, 5000);
  })
}
