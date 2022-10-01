const stars = document.querySelectorAll(".star");
const output = document.querySelector('.output');


for(let i = 0; i < stars.length; i++) {
    stars[i].starValue = i+1;
    ["click", "mouseover", "mouseout"].forEach(function(e) {
        stars[i].addEventListener(e, showrating);
    })
}

function showrating(e){
        let type = e.type;
        let starValue = this.starValue;
        if(type == "click"){
            output.innerHTML = "You rated this " + starValue + " stars.";
        }
        stars.forEach(function(elem, ind) {
            if(type === 'click'){
                console.log("I am clicked");
                if(ind < starValue) {
                    elem.classList.add("orange");
                }
                else{
                    elem.classList.remove("orange");
                }
            }  
            else if(type === "mouseover"){
                if(ind < starValue) {
                    elem.classList.add("yellow");
                }
                else{
                    elem.classList.remove("yellow");
                }
            }
            else{
                elem.classList.remove("yellow");
            }      
        })
}

function nextPage(){
    window.location.reload();
}