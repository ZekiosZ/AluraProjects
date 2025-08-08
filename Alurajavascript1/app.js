alert("Bem-vindo ao site! do número secreto");
numerosecreto=prompt("Escreva um número entre 0-10:");
while(isNaN(numerosecreto) || numerosecreto < 0 || numerosecreto > 10){
    alert("Escreva um número válido, tente novamente!");
    numerosecreto=prompt("Escreva um número:");
}
numerosecreto=Number(numerosecreto);
let numeromaquina = Math.floor(Math.random() * 11);
while (numerosecreto != numeromaquina) {
    alert("Que pena, você errou!");
    numerosecreto=prompt("Tente novamente, escreva um número entre 0-10:");
    while(isNaN(numerosecreto) || numerosecreto < 0 || numerosecreto > 10){
        alert("Escreva um número válido, tente novamente!");
        numerosecreto=prompt("Escreva um número:");
    }
}
if (numerosecreto == numeromaquina) {
    alert("Parabéns, você acertou o número secreto!");
}

