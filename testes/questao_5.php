<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      background-color: #121212;
      color: #fff;
      font-family: Arial, sans-serif;
    }
    h2 {
      color: #fff;
    }
    form {
      max-width: 300px;
      margin: 0 auto;
      padding: 20px;
      background-color: #1a1a1a;
      border-radius: 5px;
      box-shadow: 0 0 5px rgba(255, 255, 255, 0.1);
    }
    label, input[type="text"], input[type="submit"] {
      display: block;
      width: 100%;
      margin-bottom: 10px;
    }
    label {
      font-weight: bold;
    }
    input[type="text"] {
      padding: 10px;
      background-color: #333;
      border: none;
      color: #fff;
    }
    input[type="submit"] {
      padding: 10px;
      background-color: #4caf50;
      border: none;
      color: #fff;
      font-weight: bold;
      cursor: pointer;
    }
    p {
      margin-top: 20px;
    }
  </style>
</head>
<body>

<h2 style="text-align: center;">Inversor de String</h2>

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
  <label for="string">Digite a string:</label>
  <input type="text" id="string" name="string">
  <input type="submit" value="Inverter">
</form>

<?php
// Verificar se o formulário foi enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obter a string digitada pelo usuário
    $string = $_POST["string"];

    // Função para inverter os caracteres de uma string
    function inverterString($str) {
        $tamanho = strlen($str);
        $inicio = 0;
        $fim = $tamanho - 1;
        while ($inicio < $fim) {
            // Trocar os caracteres de posição
            $temp = $str[$inicio];
            $str[$inicio] = $str[$fim];
            $str[$fim] = $temp;

            // Avançar os índices de início e fim
            $inicio++;
            $fim--;
        }
        return $str;
    }

    // Chamar a função para inverter a string
    $stringInvertida = inverterString($string);

    // Exibir a string original e a string invertida
    echo "<p style='text-align: center;'>String original: " . $string . "</p>";
    echo "<p style='text-align: center;'>String invertida: " . $stringInvertida . "</p>";
}
?>

</body>
</html>