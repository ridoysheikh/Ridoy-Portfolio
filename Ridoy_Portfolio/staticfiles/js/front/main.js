let txt = [];
window.onload = fetch(`/api/?name=profession`).then(response => response.json())
.then(data => {
  data = JSON.stringify(data);
  text=JSON.parse(data).text;
  typeWriter(".profs",50,2000,text);
});


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
