var batu = document.getElementById('batu')
var kertas = document.getElementById('kertas')
var gunting = document.getElementById('gunting')
var computer = document.getElementById('computer')
var m = document.getElementById('m')
var k = document.getElementById('k')

var m_score = 0
var k_score = 0

batu.addEventListener('click' , function () {
    var x = Math.floor(Math.random() * 11);

    if(x <= 3){
        computer.src = "../img/1.png"
        alert('seri')
    }
    else if(x >= 8){
        computer.src = "../img/2.png"
        k_score += 1
        alert('kalah')
        k.innerHTML = k_score;
    }
    else{
        computer.src = "../img/3.png"
        m_score += 1
        alert('menang')
        m.innerHTML = m_score;
    }
})

kertas.addEventListener('click' , function () {
    var x = Math.floor(Math.random() * 11);

    if(x <= 3){
        computer.src = "../img/1.png"
        m_score += 1
        alert('menang')
        m.innerHTML = m_score;
        
    }
    else if(x >= 8){
        computer.src = "../img/2.png"
        alert('seri')
    }
    else{
        computer.src = "../img/3.png"
        k_score += 1
        alert('kalah')
        k.innerHTML = k_score ; 
    }
})

gunting.addEventListener('click' , function () {
    var x = Math.floor(Math.random() * 11);

    if(x <= 3){
        computer.src = "../img/1.png"
        k_score += 1
        alert('kalah')
        k.innerHTML = k_score ; 
    }
    else if(x >= 8){
        computer.src = "../img/2.png"
        m_score += 1
        alert('menang')
        m.innerHTML = m_score;
    }
    else{
        computer.src = "../img/3.png"
        alert('seri')
    }
})

batu.addEventListener('mouseover',function () {
   
})

