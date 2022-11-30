let x = "";
let buttons=document.querySelectorAll('.button');
Array.from(buttons).forEach((button)=>{
    button.addEventListener('click',(e)=>{
        if(e.targrt.innerHTML == "="){
            x=eval(x);
            document.querySelector('input').value = x;
        }
        else if(e.target.innerHTML == 'C'){
            x="";
            document.querySelector('input').value = x;
        }
        else{
            console.log(e.target)
            x=x+e.target.innerHTML;
            document.querySelector('input').value=x;
        }
    })
})