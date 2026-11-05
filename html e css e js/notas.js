const camponome = document.querySelector('#nome');
const nota01 = document.querySelector('#nota1');
const nota02 = document.querySelector('#nota2');
const nota03 = document.querySelector('#nota3');
const calcular = document.querySelector('#botaoCalcular');
const resultado = document.querySelector('#aprovacao');

calcular.addEventListener("click", () => {
    const aluno = camponome.value;
    const n1 = parseFloat(nota01.value);
    const n2 = parseFloat(nota02.value);
    const n3 = parseFloat(nota03.value);
    let media = (n1 + n2 + n3) / 3;
    let situacao = '';
    
    if (media >= 6) situacao = 'aprovado';
    else if (media >= 4) situacao = 'exame';
    else situacao = 'reprovado';
    
    resultado.textContent = `${aluno}, sua média é ${media} - situação: ${situacao}`;
});
