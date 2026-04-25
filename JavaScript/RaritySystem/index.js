let number = Math.floor(Math.random() * 100).toFixed(1);
let raridade;

if (number >= 50) {
    raridade = "Comum";
    return console.log(`Este item é ${raridade} (${number}%)`);
} else if (number >= 35) {
    raridade = "Incomum";
    return console.log(`Este item é ${raridade} (${number}%)`);
} else if (numer >= 15) {
    raridade = "Raro";
    return console.log(`Este item é ${raridade} (${number}%)`);
} else {
    raridade = "Lendário";
    return console.log(`Este item é ${raridade} (${number}%)`);
}
/*DEBUGS: 

\Projetos\JavaScript\RaritySystem> node .
Este item é Comum (97.0%)
\Projetos\JavaScript\RaritySystem> node .
Este item é Comum (85.0%)
\Projetos\JavaScript\RaritySystem> node .
Este item é Incomum (39.0%)
\Projetos\JavaScript\RaritySystem> node .
Este item é Comum (78.0%)
\Projetos\JavaScript\RaritySystem> node .
Este item é Comum (67.0%)
\Projetos\JavaScript\RaritySystem> node .
Este item é Comum (90.0%)

*/ 