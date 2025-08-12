alert("Bem-vindo ao site! do número secreto");
numerosecreto=prompt("Escreva um número entre 0-10:");
let numeromaquina = Math.floor(Math.random() * 11);
console.log("Número digitado" + numerosecreto, "Número certo" + numeromaquina);
while(isNaN(numerosecreto) || numerosecreto < 0 || numerosecreto > 10){
    console.log("Número digitado" + numerosecreto, "Número certo" + numeromaquina);
    alert("Escreva um número válido, tente novamente!");
    numerosecreto=prompt("Escreva um número:");
}
numerosecreto=Number(numerosecreto);
while (numerosecreto != numeromaquina) {
    console.log("Número digitado" + numerosecreto, "Número certo" + numeromaquina);
    alert("Que pena, você errou!");
    palavranumero = numerosecreto < numeromaquina ? "maior" : "menor"
        alert("O número secreto é "+ palavranumero + " que " + numerosecreto + "!");
    numerosecreto=prompt("Tente novamente, escreva um número entre 0-10:");
    while(isNaN(numerosecreto) || numerosecreto < 0 || numerosecreto > 10){
        alert("Escreva um número válido, tente novamente!");
        console.log("Número digitado" + numerosecreto, "Número certo" + numeromaquina);
        numerosecreto=prompt("Escreva um número:");
    }
}
if (numerosecreto == numeromaquina) {
    alert("Parabéns, você acertou o número secreto!");
}

