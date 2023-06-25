const step1 =document.querySelector('.step1')
const step2 =document.querySelector('.step2')
const prev= document.getElementById('prev');
const next= document.getElementById('next')
step2.style.display='none';
prev.style.visibility='hidden';


next.addEventListener('click', function() {
    
    step1.classList.add('animie1');
    step2.classList.remove('animie1');
    
    
    setTimeout(function() {
        step1.style.display='none'
        step2.style.display='block';
        prev.style.visibility='visible';
        next.style.display='none';
        step2.classList.add('animie2')
      }, 1000);
    })

    prev.addEventListener('click', function() {
    
        step2.classList.add('animie1');
        
        step1.classList.remove('animie1')
        setTimeout(function() {
            step1.style.display='block'
            step2.style.display='none';
            prev.style.visibility='hidden';
            next.style.display='block';
            step1.classList.add('animie2')
          }, 1000);
        })

            function slide2 (){
                step1.style.display='none';
                alert("hey")
            }