<?php

// Função para calcular a sequência de Fibonacci até um determinado número
function fibonacci($num)
{
    $fib = array(0, 1);
    while ($fib[count($fib) - 1] < $num) {
        $next = $fib[count($fib) - 1] + $fib[count($fib) - 2];
        if ($next > $num) {
            break;
        }
        $fib[] = $next;
    }
    return $fib;
}

// Número para verificar se pertence à sequência de Fibonacci
$numero = 21;

// Chamada da função fibonacci
$sequencia = fibonacci($numero);

// Verifica se o número informado pertence à sequência de Fibonacci
if (in_array($numero, $sequencia)) {
    echo "O número $numero pertence à sequência de Fibonacci.";
} else {
    echo "O número $numero não pertence à sequência de Fibonacci.";
}

?>